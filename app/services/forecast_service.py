from app.models.stacked_model import stacked_model
from app.models.stacked_model_optimatization import stacked_model_optimization
from app.models.forecast_model import evaluate_model
from app.models.forecast_model import forecast

def forecast_time_series (df_arg, frequency, steps):
    df = df_arg.copy(deep=True).reset_index(drop=True)
    
    lasso_params, enr_params, dt_params, ridge_params, best_lag = stacked_model_optimization(df, frequency, steps)
    stacked_regressor = stacked_model(lasso_params, enr_params, dt_params, ridge_params)
    
    #evaluate on training-test
    backtest_metric, predictions = evaluate_model(df, stacked_regressor, best_lag)
    
    #forecast
    out_sample_forecast = forecast(df, stacked_regressor, best_lag, steps)
    
    return backtest_metric, predictions, out_sample_forecast