import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from sklearn.metrics import mean_absolute_error, mean_squared_error
import io

def fillMissing(df):
    return df.fillna("")

def prepare_forecast_response_univariate(
    df_arg,
    tsType,
    freq,
    description,
    steps,
    forecastMethod,
    metric,
    pred_test,
    pred_out,
    result_dict,
):
    df = df_arg.copy(deep=True)

    test_size = 0.2
    test_samples = int(test_size * len(df))
    train_data, test_data = df.iloc[:-test_samples], df.iloc[-test_samples:]

    # pred_out_dict = {col: pred_out[col].to_list() for col in pred_out.columns}

    # pred_test_dict = {col: pred_test[col].to_list() for col in pred_test.columns}

    # train_data_dict = {col: train_data[col].to_list() for col in train_data.columns}

    # test_data_dict = {col: test_data[col].to_list() for col in test_data.columns}

    # df_dict = {col: df[col].to_list() for col in df.columns}

    pred_out_dict = fillMissing(pred_out).to_dict(orient="list")
    pred_out_dict["index"] = [
        date.strftime("%m/%d/%Y") for date in pd.to_datetime(pred_out.index).to_list()
    ]

    pred_test_dict = fillMissing(pred_test).to_dict(orient="list")
    pred_test_dict["index"] = [
        date.strftime("%m/%d/%Y") for date in pd.to_datetime(pred_test.index).to_list()
    ]

    train_data_dict = fillMissing(train_data).to_dict(orient="list")
    train_data_dict["index"] = [
        date.strftime("%m/%d/%Y") for date in pd.to_datetime(train_data.index).to_list()
    ]

    test_data_dict = fillMissing(test_data).to_dict(orient="list")
    test_data_dict["index"] = [
        date.strftime("%m/%d/%Y") for date in pd.to_datetime(test_data.index).to_list()
    ]

    df_dict = fillMissing(df).to_dict(orient="list")
    df_dict["index"] = [
        date.strftime("%m/%d/%Y") for date in pd.to_datetime(df.index).to_list()
    ]
    # ==========================================================
    # explanation_out_dict = describeOutForecast_univariate(
    #     forecast=pred_out, col=df.columns[0], description=description
    # )

    # # we're using the metric from backtesting.
    # error = test_data.iloc[:, 0] - pred_test.iloc[:, 0]
    # explanation_test_dict = describeTestForecast(
    #     forecast=pred_test,
    #     cols=df.columns,
    #     metrics=metric,
    #     error=error,
    #     description=description,
    # )
    # ==========================================================
    print(
        f"metrics -------------------------------------mape isffrom backtesting {metric}"
    )

    # =========================================================
    # Calculate evaluation metrics between test data and predictions
    # mae = mean_absolute_error(test_data, pred_test)
    # mse = mean_squared_error(test_data, pred_test)
    # rmse = np.sqrt(mse)
    # mape = mean_absolute_percentage_error(test_data, pred_test)

    mae = result_dict["mae"]
    mape = result_dict["mape"]
    rmse = result_dict["rmse"]
    mse = result_dict["mse"]
    # =======================================================
    response = {
        "metadata": {
            "tstype": tsType,
            "freq": freq,
            "description": description,
            "steps": steps,
            "forecast_method": forecastMethod,
            "colname": df.columns[0],
        },
        "forecast": {
            "pred_out": pred_out_dict,
            "pred_test": pred_test_dict,
            "pred_out_explanation": "",
            "pred_test_explanation": "",
            "metrics": {
                "mae": mae,
                "mse": mse,
                "rmse": rmse,
                "mape": mape,
            },
        },
        "data": {
            "train_data": train_data_dict,
            "test_data": test_data_dict,
            "entire_data": df_dict,
        },
    }

    print(response)

    return response
