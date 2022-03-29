import streamlit as st
import pandas as pd

from preprocessing import preprocess


def upload_file(file_type="xlsx"):
    return st.file_uploader("Upload csv file", type=file_type)
    
@st.cache(allow_output_mutation=True)
def load_file(data_file, file_type):
    if data_file is not None:
        if file_type=="xlsx":
            excel_file = pd.ExcelFile(data_file)
            df_mt = preprocess(pd.read_excel(excel_file, sheet_name="MT OSA"))
            df_rmt = preprocess(pd.read_excel(excel_file, sheet_name="RMT OSA"))

        return df_mt, df_rmt

def get_outlet_data(df):
    return df.groupby(list(df.columns[3:7])).count().reset_index().iloc[:, :4]    
