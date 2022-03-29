import numpy as np
import pandas as pd


def preprocess(df):
    df = format_column_names(df)
    df['WEEK'] = format_week(df['WEEK'])
    df = format_invalid_data(df)

    return df

def format_column_names(df):
    cols = ["YEAR", "MONTH", "WEEK", "AREA", "GROUP", "ACCOUNT", "OUTLET"]
    cols_df = list(df.columns[:len(cols)])
    return df.rename(columns=dict(zip(cols_df, cols)))

def format_week(week):
    return week.map(lambda x: int(str(x).split(" ")[-1]))

def format_invalid_data(df):
    def map_to_numeric(n):
        if str(n).isnumeric():
            return int(n)
        else:
            return np.NaN
        
    for col in df.columns[7:]:
        df[col] = df[col].map(map_to_numeric)
    
    return df