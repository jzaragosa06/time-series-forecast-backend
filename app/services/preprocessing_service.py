
from typing import Any
import pandas as pd
from sqlalchemy import true


def fill_missing_values(df: pd.DataFrame, method: str, value: Any = 0) -> pd.DataFrame: 
    match method:
        case "fill_with_value":
            return df.fillna(value)
        case "ffill":
            return df.fillna(method='ffill')
        case "bfill":
            return df.fillna(method='bfill')
        case "mean":
            return df.fillna(df.iloc[:,0].mean())
        case "median":
            return df.fillna(df.iloc[:,0].median())
        case "mode":
            return df.fillna(df.iloc[:,0].mode()[0])
        case _:
            return df

def drop_missing_values(df: pd.DataFrame) -> pd.DataFrame :
    return df.dropna()
