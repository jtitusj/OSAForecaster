import streamlit as st
import numpy as np

from utils import get_outlet_data

def select_data(osa_data, offtake_data):
    dataset = st.selectbox("Select Source", options=['MT', "RMT"])  

    if dataset == "MT":
        df_osa = osa_data[0]
        df_offtake = offtake_data[0]
    else: 
        df_osa = osa_data[1]
        df_offtake = offtake_data[1]

    # outlet data
    outlet = get_outlet_data(df_osa)
    out = outlet.copy()
    cols = out.columns

    area = st.selectbox("Select Area", options=out.iloc[:, 0].unique())
    out = out[out[cols[0]]==area]

    group = st.selectbox("Select Group", options=out.iloc[:, 1].unique())
    out = out[out[cols[1]]==group]

    account = st.selectbox("Select Account", options=out.iloc[:, 2].unique())
    out = out[out[cols[2]]==account]

    outlet_ = st.selectbox("Select Outlet", options=out.iloc[:, 3].unique())
    out = out[out[cols[3]]==outlet_]

    # products = st.multiselect("Select Products", options=list(df.columns[7:]),
    #                                              default=list(df.columns[7:]))

    return df_osa, df_offtake, out, cols #, products

def use_select_filter(df, out, cols):
    return np.all([df[col]==out[col].values[0] for col in cols], axis=0)
