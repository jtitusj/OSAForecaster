# Collection of utility functions
import pandas as pd
import numpy as np
import datetime

def get_int_series(series):
    """Returns extracted integer series from an object type series."""
    series = (series
              .copy()
              .astype('str')
              .str.extract(r"(\d+)")
              .astype(int))
    return series

# def get_float_series(series):
#     """Returns extracted float series from an object type series."""
#     series = (series
#               .copy()
#               .astype('str')
#               .str.extract(r"(\d+)")
#               .astype(int))
#     return series


def standardize_columns(df):
    """Returns dataframe with standardized columns"""
    return (df.rename(columns={'Week of transaction_date': 'WEEK', 
                               'OUTLET NAME': 'OUTLET',
                               'ACCOUNT/DISTRIBUTOR': 'ACCOUNT'}))

def convert_year_week_to_date(year_week_str):
    """Returns datetime of Monday of week given year and week."""
    return datetime.datetime.strptime(year_week_str + '-1', "%Y-W%W-%w")


def preprocess_raw_data(data_dict):
    """Returns preprocessed data_dict containing data frames per sheet."""
    
    data_dict = data_dict.copy()
    
    # Standardize column names
    for key in data_dict.keys():
        data_dict[key] = standardize_columns(data_dict[key])

    # Drop row without week
    for key in data_dict.keys():
        data_dict[key] = data_dict[key].dropna(subset='WEEK', axis=0)

    # Fix week number column to integer
    for key in data_dict.keys():
        data_dict[key]['WEEK'] = get_int_series(data_dict[key]['WEEK'])

    # Adding DATE column
    # Datetime of the Monday of the week
    for key in data_dict.keys():
        df = data_dict[key]
        year_week = df['YEAR'].astype('int').astype('str') + '-W' +  df['WEEK'].astype('str')
        data_dict[key]['DATE'] = year_week.apply(convert_year_week_to_date)

    # Setting Index
    for key in data_dict.keys():
        data_dict[key] = (data_dict[key]
                              .set_index(['AREA', 'GROUP', 'ACCOUNT', 'OUTLET', 'DATE'])
                              .drop(['YEAR', 'MONTH', 'WEEK'], axis=1)
                              .sort_index())
    return data_dict