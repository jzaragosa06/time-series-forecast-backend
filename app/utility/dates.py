import pandas as pd

def create_time_features(df, freq="D"):
    """
    Function to create time-based features based on the frequency of the data.

    Parameters:
    - df(pd.DataFrame): DataFrame with a DateTime index.
    - freq (str): Frequency of the data ('D', 'W', 'M', 'Q', 'Y').
                  'D' = Daily
                  'W' = Weekly
                  'M' = Monthly
                  'Q' = Quarterly
                  'Y' = Yearly

    Returns:
    - exog (pd.DataFrame): DataFrame with added time-based features.
    """

    # Ensure the index is a DateTimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("The DataFrame index must be a DateTimeIndex.")

    exog = pd.DataFrame()
    # Time-based features applicable for all frequencies
    exog["year"] = df.index.year
    exog["quarter"] = df.index.quarter

    if freq == "D":
        # Day-level features
        exog["day_of_week"] = df.index.dayofweek  # 0 = Monday, 6 = Sunday
        exog["day_of_month"] = df.index.day
        exog["day_of_year"] = df.index.dayofyear
        # exog['week_of_year'] = df.index.isocalendar().week

    elif freq == "W":
        # Week-level features
        exog["week_of_year"] = df.index.isocalendar().week
        exog["day_of_week"] = df.index.dayofweek

    elif freq == "M":
        # Month-level features
        exog["month"] = df.index.month
        exog["day_of_month"] = df.index.day

    elif freq == "Q":
        # Quarter-level features
        exog["quarter"] = df.index.quarter

    elif freq == "Y":
        # Year-level features
        exog["year"] = df.index.year

    else:
        raise ValueError("Unsupported frequency. Choose from 'D', 'W', 'M', 'Q', 'Y'.")

    return exog
