from typing_extensions import dataclass_transform
import streamlit as st
import numpy as np
import plotly.graph_objects as go

from utils import upload_file, load_file
from sidebar import select_data, use_select_filter
from plots import plot_osa, plot_offtake

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

    osa_filter = use_select_filter(df_osa, out, cols)
    outlet_osa_data = df_osa[osa_filter].sort_values(by=['YEAR', 'WEEK'])

    offtake_filter = use_select_filter(df_offtake, out, cols)
    outlet_offtake_data = df_offtake[offtake_filter].sort_values(by=['YEAR', 'WEEK'])

    time = (outlet_osa_data["YEAR"].astype(str) +
            ', Week ' +
            outlet_osa_data["WEEK"].astype(str))

    st.header("Data Overview")
    with st.expander("Show OSA Dataset", expanded=False):
        st.write(outlet_osa_data.style.format(precision=0, na_rep='NA'))

    with st.expander("Show Offtake Dataset", expanded=False):
        st.write(outlet_offtake_data.style.format(precision=2, na_rep='NA'))

    st.header("Plots")
    
    with st.expander("Show OSA Plots", expanded=False):
        products_osa = st.multiselect("Select Product(s)", options=list(df_osa.columns[7:]),
                                                    default=list(df_osa.columns[7:]),
                                                    key="osa")
        fig_osa = plot_osa(products_osa, time, outlet_osa_data)    
        st.plotly_chart(fig_osa, use_container_width=True)

    with st.expander("Show Offtake Plots", expanded=False):
        products_off = st.multiselect("Select Product(s)", options=list(df_offtake.columns[7:]),
                                                   default=list(df_offtake.columns[7:]), 
                                                   key="offtake")
        fig_offtake = plot_offtake(products_off, time, outlet_offtake_data)    
        st.plotly_chart(fig_offtake, use_container_width=True)
else:
    st.write("Please upload a dataset in the left sidebar.")