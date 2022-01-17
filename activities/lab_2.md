# Lab session 2 activities

## Activity 1: Create a html document

Create a html file. By convention the main page of a website is often called  `index.html` so you may wish to create a
file with that name.

The basic html page structure is shown below. Add this to your HTML (it may already have been created if you used an
IDE):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add page title here</title>
</head>
<body>
<!-- Add the elements here -->
</body>
</html>
```

Add the html elements listed below to the body of the html page. Add any content you wish to each of the elements.

[W3 schools HTML element reference](https://www.w3schools.com/tags/default.asp)

HTML elements to add:

```html
<title></title>
<h1></h1>
<ol></ol>
<a href=""></a>
<img src="" alt="" height="" width="">
<table>
    <tr>
        <td></td>
    </tr>
</table>
```

## Activity 2: Add CSS styling your html

Create a stylesheet called `mystyles.css`

Add a link to the stylesheet in the `<head>` section of your html, e.g.

```html

<head>
    <link rel="stylesheet" type="text/css" href="mystyles.css">
</head>
```

Add styling for the html elements you included in your html.

The general syntax is explained here: [W3Schools CSS syntax](https://www.w3schools.com/css/css_syntax.asp)

A reference for the selectors is here: [W3Schools CSS reference](https://www.w3schools.com/cssref/default.asp)

```css
h1 {
    color: plum;
    text-decoration-line: underline;
}

img {
}

ol {
}

li {
}

a {
}

table {
}

tr {
}

th {
}

td {
}
```

## Activity 3: Apply Bootstrap styling to your html

Replace your stylesheet with the [Bootstrap styles](https://getbootstrap.com/docs/5.1/getting-started/introduction/).

```html

<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
```

What does your page look like now?

Can you improve the design by applying a [grid layout](https://getbootstrap.com/docs/5.1/layout/grid/) and/or use of
the [Bootstrap examples](https://getbootstrap.com/docs/5.0/examples/)?

## Activity 4: Add HTML elements to a dash app

Open the basic dash app in [dash_app/dash_app.py](dash_app/dash_app.py).

The first line of code after the imports creates and instance of a Dash app.

The HTML layout of the page is provided in the code following `app.layout =`.

The `main` function then runs the app.

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

Run the app:

- To run the dash app from the terminal or shell make sure you are in directory of your repository and type and
  run `python dash_app.py`
- To run the dash app from PyCharm, right-click on the file name `dash_app.py` in the Project pane and
  select `Run dash_app`. Or open `dash_app.py` and click on the green run arrow near line 29.
- To run the dash app from VS Code, use the Run option from the left pane.

By default, the dash app should launch on port 8050 of your localhost with the IP address 127.0.0.1:8050. Open the
URL [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in a browser.

Note: If you get an error like this: `OSError: [Errno 48] Address already in use` then another application is already
using the default port (this will also happen if you forget to stop a previous Dash app and try to start another!). You
can try another port by modifying the line of code that runs the Dash app to specify a different port number
e.g. `app.run_server(debug=True, port=1337)`

Add the same html elements you added to the html file earlier to your dash app.

The syntax is different. See [Dash HTML components documentation](https://dash.plotly.com/dash-html-components).

Dash components are always created in the &lt;body&gt; so you will not be able to add the &lt;title&gt; element.

```python
from dash import html

html.H1(children='My title'),

html.Ol(children=[
    html.Li(children='List item 1'),
]),

html.A(children='Google', href='http://www.google.com'),

html.Img(
    src="https://www.ucl.ac.uk/cam/sites/cam/files/styles/medium_image/public/migrated-images/ucl-logo-colours-notext.gif?itok=dQiHrzS8",
    alt="UCL logo"),

html.Table(
    [
        html.Tr([
            html.Td(children='row 1 col 1'),
            html.Td(children='row 1 col 2')
        ]),
        html.Tr([
            html.Td(children='row 2 col 1'),
            html.Td(children='row 2 col 2')
        ])
    ]
),
```

## Activity 5: Add bootstrap CSS styling to the app

The `dash-bootstrap-components` library should have been installed from requirements.txt.

Apply the bootstrap styling to your dash_app e.g.:

```python
import dash
import dash_bootstrap_components as dbc
from dash import html

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Activity 6: Apply a different external stylesheet

Replace bootstrap with another external stylesheet such as [Pure.css](https://purecss.io/start/)
or [materialize](https://materializecss.com/getting-started.html) e.g.

```python
external_stylesheets = [
    {
        "href": "https://unpkg.com/purecss@2.0.6/build/pure-min.css",
        "integrity": "sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5",
        "crossorigin": "anonymous",
        "rel": "stylesheet",
    },
]
```
or
```python
external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"]
```

## Activity 7: Apply a style sheet to your coursework dash app

Apply the HTML and CSS techniques covered today to your coursework.
