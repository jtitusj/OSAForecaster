import streamlit as st
import pandas as pd

from utils import upload_file
from preprocessing import format_date
from plots import show_demand_plot

st.set_page_config(layout="wide")

st.sidebar.title("Options")
st.sidebar.header("1. Data")

with st.sidebar.expander("Dataset", expanded=False):
    use_sample = st.checkbox("Use sample data", value=True)

    if use_sample:
        df = pd.read_csv('data/df_sample.csv')
    else:    
        df = upload_file()

if df is not None:
    df = format_date(df)

    with st.sidebar.expander("Columns", expanded=False):
        col_date = st.selectbox("Date column", options=df.columns, index=0)
        col_ts = st.selectbox("Target column", options=df.columns, index=1)

st.title("Demand Forecaster")

if df is not None:
    st.header("Demand Plot")
    show_demand_plot(df, col_date, col_ts)

    st.header("Trend and Seasonality")

else:
    st.write("Input data not detected. Please upload dataset on the sidebar below or use sample data.")