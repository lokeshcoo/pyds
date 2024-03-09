import plotly.express as px
import pandas as pd

def plot_closing_graph(df, log_y=True):
    fig = px.line(df, 'Date', 'Close', title="Closing stock prices", log_y=log_y)
    return fig