import pandas as pd
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
)

from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import StackingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.model_selection import random_search_forecaster, backtesting_forecaster

def forecaster_model(model, lag):
    # Final ForecasterAutoreg
    forecaster = ForecasterAutoreg(
        regressor=model,
        lags=lag,
        transformer_y=StandardScaler(),
    )
    
    return forecaster


def evaluate_model(df_arg, model, lag): 
    df = df_arg.copy(deep=True).reset_index(drop=True)
    forecaster = forecaster_model(model, lag)
    
    backtest_metric, predictions = backtesting_forecaster(
        forecaster=forecaster,
        y=df.iloc[:, 0],
        initial_train_size=int(len(df) * 0.8),
        fixed_train_size=False,
        steps=10,
        metric="mean_squared_error",
        verbose=True,
    )

    # Compute evaluation metrics
    # y_true = df.iloc[int(len(df) * 0.8) :, 0]
    # mae = mean_absolute_error(y_true, predictions)
    # mape = mean_absolute_percentage_error(y_true, predictions)
    # mse = mean_squared_error(y_true, predictions)
    # rmse = np.sqrt(mse)
    
    # return mae, mape, mse, rmse, predictions
    
    return backtest_metric, predictions

def forecast(df_arg, model, lag, steps): 
    df = df_arg.copy(deep=True).reset_index(drop=True)
    forecaster = forecaster_model(model, lag)
    
    forecaster.fit(df.iloc[:, -1])
    out_sample_forecast = forecaster.predict(steps=steps)
    
    return out_sample_forecast
