# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
from pathlib import Path

import dash
from dash import html, Output, Input, dcc
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ------------------------------------------------------------------------
# import data
df = pd.read_excel("cleaned_tfl_dataset_EDIT.xlsx")

# create lists of travel modes
df.transport_list = df["Travel Mode"].unique().tolist()

# group dataset by recording period year
df.by_year = df.groupby(df["Period ending"].map(lambda x: x.year))
# sum the number of journeys for each year
df.by_year_sums = df.by_year.sum()
# convert index ("Period ending") to a column
df.by_year_sums.reset_index(level=0, inplace=True)
# create a list of the years
df.years_list = df.by_year_sums["Period ending"].tolist()


# create charts
fig_line = px.line(df, x="Period ending", y="Journeys (m)", color="Travel Mode",
                   title="Travel Mode Usage Over Time")
fig_pie = px.pie(df, values="Journeys (m)", names="Travel Mode", title="Distribution of Travel Modes")
fig_box = px.box(df, x="Travel Mode", y="Journeys (m)", color="Travel Mode", title="Variation in Travel Modes")
# ------------------------------------------------------------------------
# app layout

# create website header
header = [

    dbc.Row([

        dbc.Col(html.Div(
            dbc.Button("[logo]", outline=True, color="secondary"),
        ), lg=2),

        dbc.Col(html.Div([
            html.H1("TFL TRAVEL DASHBOARD")]), width={"size": 6}),

        dbc.Col(html.Div([
            dbc.Button("message", outline=True, color="secondary"),
            dbc.Button("profile", outline=True, color="secondary"),
            dbc.Button("log out", outline=True, color="secondary"),
        ],
        ), lg=4),
    ])
]

dropdown = [
    dcc.Dropdown(id="select_year",
                 options=[{"label": x, "value": x} for x in df.years_list],
                 multi=True,
                 value=2021,
                 style={'width': '40%'}
                 ),
]

checklist = [
    dcc.Checklist(id="select_travel_mode",
                  options=[{"label": x, "value": x} for x in df.transport_list],
                  ),
]

background = "#F8F9F9"

app.layout = html.Div(style={"backgroundColor": background}, children=[

    dbc.Container([

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
            html.Br()
        ),

        dbc.Row([
            dbc.Col(dropdown, lg=6, xs=12),
            dbc.Col(html.Div(id="dd_output_container")),
            dbc.Col(checklist)

        ]),

        dbc.Row(
            html.Br()
        ),

        dbc.Row([
            dbc.Col(html.Div([dcc.Graph(id="box", figure=fig_box)], style={"border": "1px Gainsboro solid"}),
                    lg=6,
                    xs=12),
            dbc.Col(html.Div([dcc.Graph(id="pie", figure=fig_pie)], style={"border": "1px Gainsboro solid"}),
                    lg=6,
                    xs=12),
            # dbc.Col(checklist)
        ]),

        dbc.Row(
            html.Br()
        ),

        dbc.Row([
            # dbc.Col(dropdown),
            dbc.Col(html.Div([dcc.Graph(id="line", figure=fig_line)], style={"border": "1px Gainsboro solid"}), lg=8,
                    xs=12),
            dbc.Col(html.Div([html.H1("LAST GRAPH")], style={"border": "1px Gainsboro solid"}))
            # dbc.Col(checklist)
        ]),

        dbc.Row(
            html.Br()
        ),

    ])
])


@app.callback(
    [Output(component_id="dd_output_container", component_property="children"),
     Output(component_id="box", component_property="figure")],
    Input(component_id="select_year", component_property="value")
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
