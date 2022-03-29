import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from plotly.subplots import make_subplots

def plot_osa(products, time, outlet_data):
    fig = make_subplots(rows=len(products), cols=1, shared_xaxes=True,
                                                    vertical_spacing=0.025)
    for i in range(len(products)):
        obj = go.Scatter(
            x = time,
            y = outlet_data[products[i]],
            mode = 'markers',
            name = products[i]
        )

        fig.add_trace(obj, row=i+1, col=1)
    
    fig.update_layout(height=200*len(products), yaxis_range=[-.05, 7.5])

    return fig