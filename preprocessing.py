import pandas as pd


def format_date(df):
    df['date'] = pd.to_datetime(df['date'])
    return df