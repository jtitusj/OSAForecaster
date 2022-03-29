import streamlit as st
import pandas as pd
import plotly.express as px


# upload csv file
def upload_file(type="csv"):
    data_file = st.file_uploader("Upload csv file", type=["csv"])
    if data_file is not None:
        return pd.read_csv(data_file)