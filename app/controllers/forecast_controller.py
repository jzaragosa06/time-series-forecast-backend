from flask import jsonify, request, Response, json
import pandas as pd
from utility import create_time_features
from utility import prepare_forecast_response_univariate
from app.services.forecast_uni import evaluate_model_then_forecast_univariate

def info():
    return jsonify({
        "message": "ts forecast info", 
    })
    
    
def forecast():
    tsType = request.form.get("type")
    freq = request.form.get("freq")
    description = request.form.get("description")
    steps = request.form.get("steps")
    forecastMethod = request.form.get("method")

    if freq not in ["D", "M", "Q", "Y"]:
        return jsonify({"message": "Format of the index is unsupported"}), 500

    file = request.files["inputFile"]
    if file:
        try:
            df = pd.read_csv(file, index_col=0, parse_dates=True)
            df.index.name = "index"
            df = df.loc[~df.index.duplicated(keep="first")]

            # fill missing values: forward fill
            df = df.ffill()
            # enforce frequency
            df = df.asfreq(freq=freq, method="ffill")

            print(df.head())

        except Exception as e:
            print(f"Error loading DataFrame: {e}")
            return jsonify({"message": f"Error loading DataFrame: {e}"}), 500

        lag = 7
        exog = create_time_features(df=df, freq=freq)

        if forecastMethod == "without_refit":
            # from here, extract the metric, pred_test, pred_out
            result = evaluate_model_then_forecast_univariate(
                df_arg=df,
                exog=exog,
                lag_value=lag,
                freq=freq,
                steps_value=int(steps),
                forecast_method="without_refit",
            )

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
    else:
        return jsonify({"message": "No csv file included"}), 500