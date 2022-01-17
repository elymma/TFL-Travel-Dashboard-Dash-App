# Introduction to Plotly Dash

## Overview

> "Dash is a Python framework for building analytical web applications. No JavaScript required. Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It’s particularly suited for anyone who works with data in Python.” — Source: Plotly website

Dash is written on top of Flask, Plotly.js, and React.js.

## How does Dash work?

Dash consists of:

- Frontend generated in Python
- Backend which is implemented on top of Flask
- Component class for every HTML tag as well as keyword arguments for all HTML arguments (`from dash import html`)
- Interactive html elements implemented (`from dash import dcc`)
- Plotly graph python API implemented in dash core components as the Graph class (`dcc.Graph`)

You declare an **app layout**. The layout will generate React.js code that will be run in the browser.

As the layout will generate HTML then it contains elements. Each element has attributes that describe its state.

Elements and attributes can be changed by interaction with the user in the browser which makes the app re-render itself.

You can listen for any changes to those attributes and run **callbacks**.

The frontend in the browser sends an HTTP request every time an input is changed.

The backend recalculates the graph of dependencies and sends back the list of changes to the frontend.

The inputs and outputs of our application interface are simply the properties of a particular component. The inputs and
outputs are described declaratively through the `app.callback` decorator.

## A basic structure for a Dash app

We will get started by building a basic Dash app in a single Python file that presents a chart but doesn’t allow any
user interaction (i.e. we will leave input/output and callbacks to a later week).

The general sequence of programming steps for a Dash app is:

1. Import the required libraries. As well as Dash itself you are likely to be using:
    - Pandas: to read and structure the data set
    - Plotly Express: to create the chart
    - Plotly Go: for more complex chart options
    - Dash Bootrap Components: to use Bootstrap styling
2. Import the dataset
3. Create the Plotly figure(s)
4. Create the app instance
5. Create the layout (and add the figures/graphs)
6. Run the server

The following shows the example in the [Dash tutorial](https://dash.plotly.com/layout).

```python
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## App layout

The following is from the [Dash layout tutorial](https://dash.plotly.com/layout).

1. The layout is composed of a tree of "components" such as html.Div and dcc.Graph.
2. The dash.html function has a component for every HTML tag. The html.H1(children='Hello Dash') component generates
   a `<h1>Hello Dash</h1>` HTML element in your application.
3. Not all components are pure HTML. The dash_core_components describe higher-level components that are interactive and
   are generated with JavaScript, HTML, and CSS through the React.js library.
4. Each component is described entirely through keyword attributes. Dash is declarative: you will primarily describe
   your application through these attributes.
5. The children property is special. By convention, it's always the first attribute which means that you can omit it:
   html.H1(children='Hello Dash') is the same as html.H1('Hello Dash'). It can contain a string, a number, a single
   component, or a list of components.

## Applying CSS stylesheets

There are several ways to apply css stylesheets.

If you place the stylesheets in the assets directory and configure the app using app = dash.Dash(__name__) then the
stylesheets will be automatically recognised.

If you wish to use one or more externally hosted stylesheets such as Materialise you can define a list and pass this as
a parameter when you execute the code. Modify the code in the Basis Dash app cell below by uncommenting the
external_stylesheets and changing the app = dash.Dash as follows:

```python
# Define the CSS style sheets to be used
external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"]

# Create a Dash app that will be configured to display the chart
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
```

## Using Bootstrap CSS with Dash

Bootstrap is a common css framework and there is a library that makes it easier to work with bootstrap in dashapps
called [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/).

This requires the library to be imported and the app to be configured slightly differently.

```python
import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
```

## Directory structure for a Dash app

A directory structure for a Dash app might be:

```
dash_app_name/
  /assets/  # An optional directory that contains CSS stylesheets and images. Dash will automatically serve all of the files that are included in this folder.
      app.css  
  /data/  # An optional directory that contains the data files (unless this is accessed via an API or database server).
      data.csv
  dash_app.py  # Contains your Dash app code and code to run the server. Sometimes named app.py or dashboard.py.
  .gitignore  # The files and folders to be ignored in git.
  requirements.txt  # The app's python dependencies.
  /venv/   # Python venv with the dependencies installed.

```

This is not the only structure you will see. For example, Dash runs as a single page app, you may however want a
multi-page app in which case you would have a sub-folder for each dash app and extract the function to run the server to
a separate file, typically run.py.

