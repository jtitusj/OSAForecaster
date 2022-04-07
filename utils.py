import streamlit as st
import pandas as pd

from preprocessing import preprocess


def upload_file(title, file_type="xlsx"):
    return st.file_uploader(title, type=file_type)
    
@st.cache(allow_output_mutation=True)
def load_file(data_file, file_type, data_source):
    if data_file is not None:
        if file_type=="xlsx":
            excel_file = pd.ExcelFile(data_file)
            df_mt = preprocess(pd.read_excel(excel_file,
                                             sheet_name=f"MT {data_source}",
                                             na_values=['NR', '-', 'NC', 'NF']))
            df_rmt = preprocess(pd.read_excel(excel_file,
                                              sheet_name=f"RMT {data_source}",
                                              na_values=['NR', '-', 'NC', 'NF']))

        return df_mt, df_rmt

def get_outlet_data(df):
    return df.groupby(list(df.columns[3:7])).count().reset_index().iloc[:, :4]