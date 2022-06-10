# Collection of utility functions
import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm

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


def get_XY(data, window_size, steps_ahead=2):
    """
    Flattens a window of data for X data and
    gives corresponding y data. 

    NOTE: for the notation "Week N", N would be relative to
    the current week of Week 0 to predict Week `steps_ahead`
    (e.g. Week 2). If the `window_size` is 4, then we 
    will consider features of Weeks 0 to Weeks -3.
    
    Args:
        data: OSA data
        window_size: Number of weeks to consider 
            for the features.
        steps_ahead: (Default: 2 weeks) Number of weeks 
            ahead to predict. 
    
    Returns:
        tuple of DataFrames (X and y)
    
    """
    XY_data = data

    # Get Features (X)
    feat = XY_data.copy()
    
    # Dropping all OSA related features
    feat = feat.drop(feat.filter(like='OSA').columns, axis=1)
    
    # Adding only one OSA feature as previous OSA
    feat['Prev OSA'] = XY_data['OSA'].values

    # One-hot encoding for categorical variables
    # Note: I made ACCOUNT, AREA etc as categorical variables
    feat = pd.get_dummies(feat)

    # Column names
    col_names = []
    for i in range(-(window_size-1), 1):
        col_names.extend(
            [f"Week {i}: {col}" for col in feat.columns]
        )

    # Get segments/windows of data and flatten them

    # Get outlets
    outlets = feat.reset_index()['OUTLET'].unique()

    result_df = []
    for outlet in tqdm(outlets):
        # Get dataframe for that outlet only
        curr_outlet = feat.loc[outlet].copy()

        # Get rows from rolling window in that outlet dataframe
        for i in range(len(curr_outlet)-window_size+1-steps_ahead):
            # Get window/segmet
            rows = curr_outlet.iloc[i:window_size+i]

            # Get index (last row with steps ahead)
            idx = (rows.iloc[-1].name)

            # Get flattened values
            values = rows.values.ravel()

            # Create flattened row
            series = pd.Series(data=values, 
                               index=col_names, 
                               name=(outlet,idx))

            result_df += [series]
    
    X_data = pd.DataFrame(result_df)

    # Remove last rows without steps ahead
    X_data.index.names = ['OUTLET', 'DATE']
#     X_data = (X_data
#               .groupby('OUTLET')
#               .apply(lambda x: x.iloc[:-steps_ahead].droplevel(0)))
    
    # Get y
    # Binary if OSA is above 95%
    y_data = (XY_data['OSA']
              .groupby('OUTLET')
              .shift(-steps_ahead)
              .groupby('OUTLET')
              .apply(lambda x: x.iloc[window_size-1:])
              .dropna() >= 0.95)
    y_data.name = f'Week +{steps_ahead}: OSA>=95%'

    
    return X_data, y_data