from typing import Dict
import pandas as pd


# def convert_to_list_of_dict(df: pd.DataFrame):
#     return [{str(idx): val} for idx, val in df[:, 0].items()]

# def convert_series_to_list_of_dict(series: pd.Series):
#     return [{str(idx): val} for idx, val in series.items()]

def convert_series_to_list_of_dict(series: pd.Series):
    return [{"index": idx, "value": val} for idx, val in series.items()]

def convert_to_list_of_dict(df: pd.DataFrame):
    return [{"index": idx, "value": val} for idx, val in df[df.columns[0]].items()]