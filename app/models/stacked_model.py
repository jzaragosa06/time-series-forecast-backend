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

def stacked_model(lasso_params, enr_params, dt_params, ridge_params):    
    # Recreate optimized StackingRegressor
    lasso = Lasso(**lasso_params)
    enr  = ElasticNet(**enr_params)
    dt  = DecisionTreeRegressor(**dt_params, random_state=123)
    ridge = Ridge(**ridge_params, random_state=123)
    
    stacked_regressor = StackingRegressor(
        estimators=[("lasso", lasso), ("enr", enr), ("dt", dt)],
        final_estimator=ridge,
    )
    
    return stacked_regressor

