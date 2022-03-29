import streamlit as st

from utils import get_outlet_data

def select_data(dfs):
    dataset = st.selectbox("Select Source", options=['MT', "RMT"])  

    if dataset == "MT":
        df = dfs[0]
    else: 
        df = dfs[1] 

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

    products = st.multiselect("Select Products", options=list(df.columns[7:]),
                                                 default=list(df.columns[7:]))

    return df, out, col, products
