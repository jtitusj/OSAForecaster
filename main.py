from typing_extensions import dataclass_transform
import streamlit as st
import numpy as np
import plotly.graph_objects as go

from utils import upload_file, load_file
from sidebar import select_data
from plots import plot_osa

st.set_page_config(layout="wide")

st.sidebar.title("Options")
st.sidebar.header("1. Data")

with st.sidebar.expander("Prepare Data", expanded=False):
    file_type = "xlsx"

    # osa
    osa_file = upload_file("Upload OSA data", file_type)
    osa_data = load_file(osa_file, file_type, data_source="OSA")

    # offtake
    offtake_file = upload_file("Upload Offtake data", file_type)
    offtake_data = load_file(offtake_file, file_type, data_source="OFFTAKE")

st.title("On-Shelf Availability Forecaster")

if osa_data is not None and offtake_data is not None:

    with st.sidebar.expander("Filter", expanded=True):
        df_osa, df_offtake, out, cols = select_data(osa_data, offtake_data)

    filters = np.all([df_osa[col]==out[col].values[0] for col in cols], axis=0)
    outlet_data = df_osa[filters].sort_values(by=['YEAR', 'WEEK'])

    time = outlet_data["YEAR"].astype(str) + ', Week ' + outlet_data["WEEK"].astype(str)

    st.header("Data Overview")
    with st.expander("Show Dataset", expanded=False):
        # st.write(outlet_data.loc[:, ['YEAR', 'MONTH', 'WEEK', 'OUTLET'] + products])
        st.write(outlet_data)

    st.header("On-Shelf Availability Plots")
    products = st.multiselect("Select Product(s)", options=list(df_osa.columns[7:]),
                                                   default=list(df_osa.columns[7:]))
    
    with st.expander("Show Plots", expanded=False):
        fig = plot_osa(products, time, outlet_data)    
        st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Please upload a dataset in the left sidebar.")