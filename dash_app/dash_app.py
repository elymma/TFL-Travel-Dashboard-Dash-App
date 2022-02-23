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
    dcc.Dropdown(id="select-year",
                 options=[{"label": x, "value": x} for x in df.years_list],
                 multi=True,
                 value=df.years_list[0],
                 style={'width': '60%'}
                 ),
]

checklist = [
    dcc.Checklist(id="select-travel-mode",
                  options=[{"label": x, "value": x} for x in df.transport_list],
                  labelStyle={'display': 'inline-block'},
                  style={'width': '60%'}

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

        dbc.Row([
            dbc.Col(dropdown, lg=6, xs=12),
            dbc.Col(html.Div(id="dd_output_container")),
            # dbc.Col(checklist)
        ]),

        dbc.Row(
            html.Br()
        ),

        dbc.Row([
            dbc.Col(html.Div([dcc.Graph(id="line", figure=fig_line)], style={"border": "1px Gainsboro solid"}), lg=8,
                    xs=12),
            dbc.Col(html.Div(
                html.Div(id="stats-card", style={"border": "1px Gainsboro solid"})))
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
        ]),

        dbc.Row(
            html.Br()
        ),

    ])
])


@app.callback([Output("box", "figure"),
               Output("pie", "figure"),
               Output("line", "figure"),
               Output("stats-card", "children")],
              Input("select-year", "value"))
def update_tfl_chart(year_select):
    # create copy of data set
    # df.chosen_travel_mode = df.copy()
    # select data for chosen travel mode
    # df.total_travel = []
    # if travel_select is not None:
    #    for x in travel_select:
    #        df.chosen_travel = df[df["Travel Mode"].str.contains(x)]
    #        df.total_travel.append(df.chosen_travel)
    # create a copy of the travel-sorted dataset
    # df.chosen_year = df.total_travel.copy()

    # create a copy of dataset
    df.chosen_year = df.copy()
    # select data for chosen year
    if type(year_select) != int:
        # when there is a list of year values
        df.chosen_year = df.chosen_year[df.chosen_year["Period ending"].dt.year.isin(year_select)]
    else:
        # when there is only one year value
        df.chosen_year = df.chosen_year[df.chosen_year["Period ending"].dt.year == year_select]
    # create figures
    fig_box_update = px.box(df.chosen_year, x="Travel Mode", y="Journeys (m)", color="Travel Mode",
                            title="Variation in Travel Modes<br><sup>Year(s) shown: {}</sup>".format(year_select))
    fig_pie_update = px.pie(df.chosen_year, values="Journeys (m)", names="Travel Mode",
                            title="Distribution of Travel Modes<br><sup>Year(s) shown: {}</sup>".format(year_select))
    fig_line_update = px.line(df.chosen_year, x="Period ending", y="Journeys (m)", color="Travel Mode",
                              title="Travel Mode Usage Over Time<br><sup>Year(s) shown: {}</sup>".format(year_select))
    # order data in descending/ascending order
    desc_order = df.chosen_year.sort_values("Journeys (m)", ascending=False)
    asc_order = df.chosen_year.sort_values("Journeys (m)", ascending=True)
    # find the highest and lowest recording periods
    max_journeys = desc_order.iloc[0, 4]
    max_period_b = desc_order.iloc[0, 1]
    max_period_e = desc_order.iloc[0, 2]
    max_mode = desc_order.iloc[0, 3]

    lowest = asc_order.iloc[0, 4]
    # create stats card
    stats_card = dbc.Card(className="bg-dark text-light", children=[
        dbc.CardBody([
            html.H4(year_select, id="card-name", className="card-title"),
            html.Br(),
            html.H6("High is:", className="card-title"),
            html.H4("The recording period with the most journeys was {} to {} with {} million journeys using the {}".format(max_period_b, max_period_e, max_journeys, max_mode), className="card-text text-light"),
            html.Br(),
            html.H6("Low is:", className="card-title"),
            html.H4("lowest {}".format(lowest), className="card-text text-light"),
            html.Br(),

        ])
    ])

    return fig_box_update, fig_pie_update, fig_line_update, stats_card


if __name__ == '__main__':
    app.run_server(debug=True)
