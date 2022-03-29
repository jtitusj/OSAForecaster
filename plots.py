import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def show_demand_plot(df, col_date, col_ts):
    fig = go.Figure()

    obj_main = go.Scatter(
        x = df[col_date],
        y = df[col_ts],
        mode = 'lines',
        name = 'demand'
    )

    # moving average
    window = st.number_input("Input window size for moving average", min_value=0, value=0)
    df_ma = df.set_index('date').rolling(window).mean().dropna().reset_index()
    obj_ma = go.Scatter(
        x = df_ma[col_date],
        y = df_ma[col_ts],
        mode = 'lines',
        name = f'ma({window})'
    )

    fig.add_trace(obj_main)
    fig.add_trace(obj_ma)

    fig.update_layout(
        title=f"Sales/Demand for {col_ts}",
        xaxis_title="Date",
        yaxis_title="Demand",
        legend_title="Legend",
        # font=dict(
        #     family="Courier New, monospace",
        #     size=18,
        #     color="RebeccaPurple"
        # )
    )
    st.plotly_chart(fig, use_container_width=True)