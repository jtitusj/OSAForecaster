import numpy as np
import pandas as pd


def preprocess(df):
    df = format_column_names(df)
    df = remove_total_row(df)
    df['YEAR'] = format_year_column(df['YEAR'])
    df['WEEK'] = format_week_column(df['WEEK'])
    df = format_invalid_data(df)

    return df

def format_column_names(df):
    cols = ["YEAR", "MONTH", "WEEK", "AREA", "GROUP", "ACCOUNT", "OUTLET"]
    cols_df = list(df.columns[:len(cols)])
    return df.rename(columns=dict(zip(cols_df, cols)))

def remove_total_row(df):
    "Remove row if it contains sums of previous value"
    return df[df["OUTLET"] != "TOTAL"]

def format_year_column(year):
    return year.astype(int)

def format_week_column(week):
    return week.map(lambda x: int(str(x).split(" ")[-1]))

def format_invalid_data(df):
    def map_to_numeric(n):
        if n in ['NR', '-', 'NC', 'NF']:
            return np.NaN   
        else:
            return float(n)
        
    for col in df.columns[7:]:
        df[col] = df[col].map(map_to_numeric)
    
    return df