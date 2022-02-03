# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
from pathlib import Path

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# ------------------------------------------------------------------------
# import data and create chart

df = pd.read_excel("cleaned_tfl_dataset_EDIT.xlsx")

fig = px.area(df, x="Period ending", y="Journeys (m)", color="Travel Mode", title="Distribution of TFL Travel Modes")

fig.show()

# ------------------------------------------------------------------------
# app layout

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.H2("hI"),

    dcc.Graph(id="graph"),

])

if __name__ == '__main__':
    app.run_server(debug=True)
