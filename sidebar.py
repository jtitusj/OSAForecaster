import streamlit as st

from preprocessing import format_column_names, format_invalid_data
from utils import get_outlet_data

def select_data(df):
    df = format_column_names(df)
    df = format_invalid_data(df)

    # outlet data
    outlet = get_outlet_data(df)
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

    return df, out, col
