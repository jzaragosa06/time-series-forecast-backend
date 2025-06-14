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

def stacked_model_optimization(df_arg, frequency, steps, lag=7):
    df = df_arg.copy(deep=True).reset_index(drop=True)
    
    # Define base and meta estimators for StackingRegressor
    base_estimators = [
        ("lasso", Lasso(random_state=123)),
        ("enr", ElasticNet(random_state=123)),
        ("dt", DecisionTreeRegressor(random_state=123)),
    ]
    meta_estimator = Ridge(random_state=123)
    
    stacking_regressor = StackingRegressor(
        estimators=base_estimators, final_estimator=meta_estimator
    )
    
    # Initialize the ForecasterAutoreg
    forecaster = ForecasterAutoreg(
        regressor=stacking_regressor,
        lags=lag,
        transformer_y=StandardScaler(),
        transformer_exog=StandardScaler(),
    )

    # Define hyperparameter grid for random search
    param_grid = {
        "lasso__alpha": [0.001, 0.01, 0.1, 1, 10, 100],
        "lasso__max_iter": [500, 1000, 1500],
        "enr__alpha": [0.001, 0.01, 0.1, 1.0, 10.0],
        "enr__l1_ratio": [0.1, 0.5, 0.7, 0.9, 1.0],
        "dt__max_depth": [3, 5, 10, None],
        "dt__min_samples_split": [2, 5, 10],
        "dt__min_samples_leaf": [1, 2, 4],
        "dt__max_features": [None, "sqrt", "log2"],
        "final_estimator__alpha": [0.01, 0.1, 1, 10, 100],
        "final_estimator__fit_intercept": [True, False],
        "final_estimator__solver": ["auto", "svd", "cholesky", "lsqr", "saga"],
    }
    
    # Perform random search with verbose output
    search_results = random_search_forecaster(
        forecaster=forecaster,
        y=df.iloc[:, 0],  # Time series data
        param_distributions=param_grid,
        lags_grid=[3, 5, 7, 12, 14],
        steps=10,
        n_iter=10,
        metric="mean_squared_error",
        initial_train_size=int(len(df) * 0.8),
        fixed_train_size=False,
        refit=True, # this will perform a backtesting on different split, where the model refit every increase in training size. 
        return_best=True,
        random_state=123,
        verbose=True,
    )

    best_params = search_results.iloc[0]["params"]
    lasso_params = {
        k.replace("lasso__", ""): v for k, v in best_params.items() if "lasso__" in k
    }
    enr_params = {
        k.replace("enr__", ""): v for k, v in best_params.items() if "enr__" in k
    }
    dt_params = {
        k.replace("dt__", ""): v for k, v in best_params.items() if "dt__" in k
    }
    ridge_params = {
        k.replace("final_estimator__", ""): v
        for k, v in best_params.items()
        if "final_estimator__" in k
    }

    best_lag = int(max(list(search_results.iloc[0]["lags"])))

    return lasso_params, enr_params, dt_params, ridge_params, best_lag