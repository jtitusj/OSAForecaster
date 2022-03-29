import numpy as np
import pandas as pd


def format_column_names(df):
    cols = ["YEAR", "MONTH", "WEEK", "AREA", "GROUP", "ACCOUNT", "OUTLET"]
    cols_df = list(df.columns[:len(cols)])
    return df.rename(columns=dict(zip(cols_df, cols)))

def format_week(week):
    return week.map(lambda x: int(str(x).split(" ")[-1]))

def format_invalid_data(df):
    cols = list(df.columns[7:])

    def mapToNan(n):
        if str(n).isnumeric():
            return n
        else:
            return np.NaN

    for col in cols:
        df[col] = df[col].map(mapToNan)

    return df

def format_date(df):
    df['date'] = pd.to_datetime(df['date'])
    return df