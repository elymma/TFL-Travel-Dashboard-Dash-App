# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
from pathlib import Path

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ------------------------------------------------------------------------
# import data and create chart

df = pd.read_excel("cleaned_tfl_dataset_EDIT.xlsx")

fig_line = px.line(df, x="Period ending", y="Journeys (m)", color="Travel Mode", title="Distribution of TFL Travel Modes")

fig_pie = px.pie(df, values="Journeys (m)", names="Travel Mode")
# ------------------------------------------------------------------------
# app layout

header = [

    dbc.Col(html.Div(
        dbc.Button("logo", outline=True, color="primary"),
    ), width=2),
    dbc.Col(html.Div([
        dbc.Button("message", outline=True, color="primary"), dbc.Button("profile", outline=True, color="primary"), dbc.Button("log out", outline=True, color="primary"),
    ],
    ), width=3),
]

app.layout = html.Div(children=[

    dbc.Row(
        header,
        justify="between",


    ),

    dbc.Row(
        dcc.Dropdown(id="select_year",
                     options=[
                         {'label': '2010', 'value': 2010},
                         {'label': '2011', 'value': 2011},
                         {'label': '2012', 'value': 2012},
                         {'label': '2013', 'value': 2013},
                         {'label': '2014', 'value': 2014},
                         {'label': '2015', 'value': 2015},
                         {'label': '2016', 'value': 2016},
                         {'label': '2017', 'value': 2017},
                         {'label': '2018', 'value': 2018},
                         {'label': '2019', 'value': 2019},
                         {'label': '2020', 'value': 2020},
                         {'label': '2021', 'value': 2021},
                     ],
                     style={'width': '40%'}
                     ),

    ),

    dbc.Row([

        dcc.Graph(id="graph", figure=fig_line),
        dcc.Graph(id="graph_two", figure=fig_pie),
    ],


    ),

    dbc.Row(

        dcc.Checklist(id="select_travel_mode",
                      options=[
                          {'label': 'Bus', 'value': 'Bus'},
                          {'label': 'Underground', 'value': 'Underground'},
                          {'label': 'DLR', 'value': 'DLR'},
                          {'label': 'Tram', 'value': 'Tram'},
                          {'label': 'Overground', 'value': 'Overground'},
                          {'label': 'Emirates Airline', 'value': 'Emirates Airline'},
                          {'label': 'TFL Rail', 'value': 'TFL Rail'},
                      ],

                      ),

    ),

])


# @app.callback(
#    Output(component_id='my-output', component_property='children'),
#    Input(component_id='my-input', component_property='value')
# )
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
