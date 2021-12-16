import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import flask
import os
import argparse


# Boilerplate starts here

parser = argparse.ArgumentParser(description='A simple example of a Dash app.')
parser.add_argument('-d', '--deploy', action='store_true',
                    help='the app is in a deployed environment')

DEPLOY = parser.parse_args().deploy

if DEPLOY:
    app = dash.Dash('app', external_stylesheets=[dbc.themes.BOOTSTRAP])
else:
    print('Here!')
    # Set up for JupyterLab development
    server = flask.Flask('app')
    server.secret_key = os.environ.get('secret_key', 'secret')
    app = dash.Dash('app', server=server, url_base_pathname='/_tunnel_/8050/', 
                    external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.scripts.config.serve_locally = False


# App starts here

app.layout = html.Div(
    dbc.Container([
        dbc.Row(html.H1('Old Faithful Geyser Data')),

        dbc.Row([
            dbc.Col(
                [
                    html.H4('Number of bins'),
                    dcc.Slider(
                        id = 'bins',
                        min = 1,
                        max = 50,
                        value = 30,
                        marks = {x: x for x in range(5, 51, 5)}
                    )
                ],
                width = 3,
                align = 'center'
            ),

            dbc.Col(
                dcc.Graph(
                    id = 'faithful-graph',
                ),
                width = 9
            )
        ])
    ])
)


@app.callback(
    dash.dependencies.Output('faithful-graph', 'figure'),
    [dash.dependencies.Input('bins', 'value')]
)
def update_figure(number_of_bins):
    faithful_waiting = [79, 54, 74, 62, 85, 55, 88, 85, 51, 85, 54, 84, 78, 47, 83,
                        52, 62, 84, 52, 79, 51, 47, 78, 69, 74, 83, 55, 76, 78, 79,
                        73, 77, 66, 80, 74, 52, 48, 80, 59, 90, 80, 58, 84, 58, 73,
                        83, 64, 53, 82, 59, 75, 90, 54, 80, 54, 83, 71, 64, 77, 81,
                        59, 84, 48, 82, 60, 92, 78, 78, 65, 73, 82, 56, 79, 71, 62,
                        76, 60, 78, 76, 83, 75, 82, 70, 65, 73, 88, 76, 80, 48, 86,
                        60, 90, 50, 78, 63, 72, 84, 75, 51, 82, 62, 88, 49, 83, 81,
                        47, 84, 52, 86, 81, 75, 59, 89, 79, 59, 81, 50, 85, 59, 87,
                        53, 69, 77, 56, 88, 81, 45, 82, 55, 90, 45, 83, 56, 89, 46,
                        82, 51, 86, 53, 79, 81, 60, 82, 77, 76, 59, 80, 49, 96, 53,
                        77, 77, 65, 81, 71, 70, 81, 93, 53, 89, 45, 86, 58, 78, 66,
                        76, 63, 88, 52, 93, 49, 57, 77, 68, 81, 81, 73, 50, 85, 74,
                        55, 77, 83, 83, 51, 78, 84, 46, 83, 55, 81, 57, 76, 84, 77,
                        81, 87, 77, 51, 78, 60, 82, 91, 53, 78, 46, 77, 84, 49, 83,
                        71, 80, 49, 75, 64, 76, 53, 94, 55, 76, 50, 82, 54, 75, 78,
                        79, 78, 78, 70, 79, 70, 54, 86, 50, 90, 54, 54, 77, 79, 64,
                        75, 47, 86, 63, 85, 82, 57, 82, 67, 74, 54, 83, 73, 73, 88,
                        80, 71, 83, 56, 79, 78, 84, 58, 83, 43, 60, 75, 81, 46, 90,
                        46, 74]

    return go.Figure(
        data = [
            go.Histogram(
                x = faithful_waiting,
                xbins = {
                    'start': min(faithful_waiting),
                    'end': max(faithful_waiting) + 1,
                    'size': (max(faithful_waiting) + 1 -
                             min(faithful_waiting)) / number_of_bins
                }
            )
        ],
        layout=go.Layout(
            xaxis = {'title': 'Waiting time'},
            yaxis = {'title': 'Frequency'}
        )

    )


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=80 if DEPLOY else 8050)
