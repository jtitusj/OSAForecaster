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
    data_file = upload_file(file_type)
    dataframes = load_file(data_file, file_type)

st.title("On-Shelf Availability Forecaster")

if dataframes is not None:

    with st.sidebar.expander("Filter", expanded=True):
        df, out, cols = select_data(dataframes)

    filters = np.all([df[col]==out[col].values[0] for col in cols], axis=0)
    outlet_data = df[filters].sort_values(by=['YEAR', 'WEEK'])

    time = outlet_data["YEAR"].astype(str) + ', Week ' + outlet_data["WEEK"].astype(str)

    st.header("Data Overview")
    with st.expander("Show Dataset", expanded=True):
        # st.write(outlet_data.loc[:, ['YEAR', 'MONTH', 'WEEK', 'OUTLET'] + products])
        st.write(outlet_data)

    st.header("OSA Plots")
    products = st.multiselect("Select Product(s)", options=list(df.columns[7:]),
                                                   default=list(df.columns[7:]))
    
    fig = plot_osa(products, time, outlet_data)    

    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Please upload a dataset in the left sidebar.")