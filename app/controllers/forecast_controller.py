from flask import jsonify, request, Response, json
import pandas as pd
from app.services.forecast_service import forecast_time_series

def info():
    return jsonify({
        "message": "ts forecast info", 
    })

def forecast():
    data = request.get_json()
    
    #retrieve data
    frequency = data.get('frequency')
    steps = data.get('steps')
    forecast_method = data.get('forecast_method')
    series = data.get('series', [])

    if not all([series, frequency, steps, forecast_method]): 
        return jsonify({"message": "The data is malformed"}), 400

    #series->DataFrame obj
    series_flat_dict = {k: v for d in series for k, v in d.items()}

    df = pd.DataFrame.from_dict(series_flat_dict, orient='index', columns=['value'])

    try:
        backtest_metric, predictions, out_sample_forecast = forecast_time_series(df, frequency, steps)
        return jsonify(
            {
                "message": "Forecast run successfully", 
                "metric": backtest_metric.to_dict(orient="records"), 
                # "predictions": predictions.to_dict(orient="records"), 
                "predictions": predictions.to_dict(), 
                "out_sample_forecast": out_sample_forecast.to_dict(),
            }
        ), 200
    except Exception as e:
        print('An exception occurred')
        return jsonify({"message":  "Error occured while running forecast",  "error": e })
