from turtle import clear, width
import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/about-us")

layout = html.Div(
    dbc.Container(
        [
            html.H1("About us", className="display-3"),
            
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/fernando.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Fernando Mendoza", className="card-title"),
                html.P(
                    "Químico - Ingeniero químico",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/fernando-mendoza-rangel-aa81b2142", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/caro.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Carolay Helena Meza", className="card-title"),
                html.P(
                    "Administradora de Mercadeo",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/carolay-helena-meza-mesa-078a69226/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/mathilda.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Mathilda Campillo", className="card-title"),
                html.P(
                    "Matemática",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/mathilda-campillo-abuchaibe-9538b2235/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/jhonatan.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Jhonatan Archila", className="card-title"),
                html.P(
                    "Ingeniero Agrícola",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/jhonatanarchila/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                        ]
                    ),
                ]
            ),

            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/sebastian.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Sebastian Chaparro", className="card-title"),
                html.P(
                    "Magister en ingeniería de sistemas y computación",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/sebastian-chaparro-079b2a157/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/diego.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Diego Castañeda", className="card-title"),
                html.P(
                    "Estadístico",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/diegofercas/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/juan.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Juan Pablo Martínez", className="card-title"),
                html.P(
                    "Profesión",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/juan-pablo-mart%C3%ADnez-betancur-8a62611b0/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                            dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/assets/imgs/david.png", top=True),
        dbc.CardBody(
            [
                html.H4("David Vargas", className="card-title"),
                html.P(
                    "Ingeniero de sistemas y computación",
                    className="card-text",
                ),
                dbc.Button("LinkedIn Profile", color="success", href="https://www.linkedin.com/in/dvargasvalencia/", external_link=True, target="_blank",),
            ]
        ),
    ],
    style={"width": "18rem"},
),),
                        ]
                    ),
                ]
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