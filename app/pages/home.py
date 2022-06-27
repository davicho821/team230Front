import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div(
    dbc.Container(
        [
            #html.H1("Breast Cancer", className="display-3"),
            dbc.Carousel(
            items=[
                {"key": "1", "src": "/assets/imgs/slide01.jpg"},
                #{"key": "2", "src": "/assets/imgs/slide02.jpg"},
                #{"key": "3", "src": "/assets/imgs/slide03.jpg"},
            ],
            #controls=True,
            #indicators=False,
            #interval=5000,
            ride="carousel",
            ),
            html.P(
                "Here goes main information...",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Here goes main information...",
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)