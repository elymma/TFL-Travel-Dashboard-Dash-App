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
# import data and create charts

df = pd.read_excel("cleaned_tfl_dataset_EDIT.xlsx")

fig_line = px.line(df, x="Period ending", y="Journeys (m)", color="Travel Mode",
                   title="Travel Mode Usage Over Time")

fig_pie = px.pie(df, values="Journeys (m)", names="Travel Mode", title="Distribution of Travel Modes")

fig_box = px.box(df, x="Travel Mode", y="Journeys (m)", color="Travel Mode", title="Variation in Travel Modes")
# ------------------------------------------------------------------------
# app layout

header = [

    dbc.Col(html.Div(
        dbc.Button("logo", outline=True, color="primary"),
    ), width=2),
    dbc.Col(html.Div([
        dbc.Button("message", outline=True, color="primary"), dbc.Button("profile", outline=True, color="primary"),
        dbc.Button("log out", outline=True, color="primary"),
    ],
    ), width=3),
]

dropdown = [
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
]

checklist = {
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

}

app.layout = html.Div(children=[

    dbc.Row(
        html.Br()
    ),

    dbc.Row(
        header,
        justify="between",
    ),

    dbc.Row(
        html.Br()
    ),

    dbc.Row(
        html.Div([
            html.H1("TFL TRAVEL DASHBOARD")
        ], style={"border": "1px black solid"})
    ),

    dbc.Row(
        html.Br()
    ),

    dbc.Row([
        dbc.Col(dropdown),
        dbc.Col(html.Div(id="dd_output_container"))

    ]),

    dbc.Row([
        dbc.Col(html.Div([dcc.Graph(id="graph_three", figure=fig_box)]), lg=6, xs=12),
        dbc.Col(html.Div([dcc.Graph(id="graph_two", figure=fig_pie)]), lg=6, xs=12),
        # dbc.Col(checklist)
    ]),

    dbc.Row([
        # dbc.Col(dropdown),
        dbc.Col(html.Div([dcc.Graph(id="graph", figure=fig_line)]), lg=8, xs=12),
        dbc.Col(html.Div([html.H1("LAST GRAPH")], style={"border": "1px black solid"}))
        # dbc.Col(checklist)
    ]),

])


@app.callback(
    Output(component_id="dd_output_container", component_property="children"),
    Input(component_id="select_year", component_property="value")

)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
