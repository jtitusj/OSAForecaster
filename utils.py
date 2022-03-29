import streamlit as st
import pandas as pd


# upload csv file
def upload_file(file_type="xlsx"):
    data_file = st.file_uploader("Upload csv file", type=file_type)
    if data_file is not None:
        if file_type=="xlsx":
            excel_file = pd.ExcelFile(data_file)
            df_mt = pd.read_excel(excel_file, sheet_name="MT OSA")
            df_rmt = pd.read_excel(excel_file, sheet_name="RMT OSA")

        return df_mt, df_rmt

def get_outlet_data(df):
    return df.groupby(list(df.columns[3:7])).count().reset_index().iloc[:, :4]    
