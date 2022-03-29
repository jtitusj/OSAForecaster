import numpy as np
import pandas as pd


def format_invalid_data(df):
    cols = list(df.columns[7:])

    def mapToNan(n):
        if not str(n).isnumeric():
            return np.NaN
    for col in cols:
        df[col] = df[col].map(mapToNan)

    return df

def format_date(df):
    df['date'] = pd.to_datetime(df['date'])
    return df