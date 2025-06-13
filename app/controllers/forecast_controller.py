from flask import jsonify, request, Response, json
import pandas as pd
from utility import create_time_features
from utility import prepare_forecast_response_univariate
from app.services.forecast_service import evaluate_model_then_forecast_univariate

def info():
    return jsonify({
        "message": "ts forecast info", 
    })
    

def forecast():
    
    #retrieve data
    frequency = request.form.get("freq")
    data_context = request.form.get("data_context")
    steps = request.form.get("steps")
    forecast_method = request.form.get("method")
    
    #series (F: array of object, B: list of dictionaries)
    series_data = request.form.get("series")
    
    if not all([series_data, frequency, steps, forecast_method]): 
        return jsonify({"message": "The data is malformed"}), 400

    #series->DataFrame obj
    df= pd.DataFrame(series_data)

    # from here, extract the metric, pred_test, pred_out
    result = evaluate_model_then_forecast_univariate(
        df_arg=df,
        exog=exog,
        lag_value=lag,
        freq=freq,
        steps_value=int(steps),
        forecast_method="without_refit",
    )
    
    #base model training
    
    #stacking model trainign
    
    #prediciton 
    
    #return: list of dictionary for result

    #-------------------------------------------
    try:
        response = prepare_forecast_response_univariate(
            df_arg=df,
            tsType=tsType,
            freq=freq,
            description=description,
            steps=int(steps),
            forecastMethod=forecastMethod,
            metric=result["mape"],
            pred_test=result["pred_test"],
            pred_out=result["pred_out"],
            result_dict=result,
        )

        return Response(json.dumps(response), mimetype="application/json")
    except Exception as e:
        print(f"Error in preparing response: {e}")
        return jsonify({"message": f"Error in preparing response: {e}"}), 500