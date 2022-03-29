import streamlit as st

from preprocessing import format_column_names, format_invalid_data, format_week
from utils import get_outlet_data

def select_data(dfs):
    dataset = st.selectbox("Select Source", options=['MT', "RMT"])  
    df = None

    if dataset == "MT":
        df = dfs[0]
    else: 
        df = dfs[1] 

    # preprocess
    df_ = format_column_names(df)
    df_['WEEK'] = format_week(df_['WEEK'])
    df_ = format_invalid_data(df_)

    # outlet data
    outlet = get_outlet_data(df_)
    out = outlet.copy()
    col = out.columns

    area = st.selectbox("Select Area", options=out.iloc[:, 0].unique())
    out = out[out[col[0]]==area]

    group = st.selectbox("Select Group", options=out.iloc[:, 1].unique())
    out = out[out[col[1]]==group]

    account = st.selectbox("Select Account", options=out.iloc[:, 2].unique())
    out = out[out[col[2]]==account]

    outlet_ = st.selectbox("Select Outlet", options=out.iloc[:, 3].unique())
    out = out[out[col[3]]==outlet_]

    return df_, out, col
