from flask import jsonify, request, Response, json
import pandas as pd
from app.services.forecast_service import forecast_time_series
from app.utility.series import convert_series_to_list_of_dict, convert_to_flat_dict, convert_to_list_of_dict

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
    series_flat_dict = convert_to_flat_dict(series)

    df = pd.DataFrame.from_dict(series_flat_dict, orient='index', columns=['value'])

    try:
        backtest_metric, predictions, out_sample_forecast = forecast_time_series(df, frequency, steps)
        return jsonify(
            {
                "message": "Forecast run successfully", 
                "metric": backtest_metric.to_dict(orient="records"), 
                "in_sample_forecast_test": convert_to_list_of_dict(predictions), 
                "out_sample_forecast": convert_series_to_list_of_dict(out_sample_forecast),
            }
        ), 200
    except Exception as e:
        print('An exception occurred')
        return jsonify({"message":  "Error occured while running forecast",  "error": e })
