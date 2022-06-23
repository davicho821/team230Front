from turtle import width
import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/about-us")

layout = html.Div(
    dbc.Container(
        [
            html.H1("About us", className="display-3"),
            html.P(
                "Here goes main information...",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Here goes main information...",
            ),
            
            dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                src="/assets/imgs/carolay.jpg",
                                className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4("Carolay Helena", className="card-title"),
                                    html.P(
                                        "This is a wider card with supporting text "
                                        "below as a natural lead-in to additional "
                                        "content. This content is a bit longer.",
                                        className="card-text",
                                    ),
                                    html.Small(
                                        "LinkedIn Profile",
                                        className="card-text text-muted",
                                    ),
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],                                  
    className="mb-3",
    style={"maxWidth": "540px"},
),

            dbc.Card(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.CardImg(
                                            src="/assets/imgs/mathilda.jpg",
                                            className="img-fluid rounded-start",
                                        ),
                                        className="col-md-4",
                                    ),
                                    dbc.Col(
                                        dbc.CardBody(
                                            [
                                                html.H4("Mathilda", className="card-title"),
                                                html.P(
                                                    "This is a wider card with supporting text "
                                                    "below as a natural lead-in to additional "
                                                    "content. This content is a bit longer.",
                                                    className="card-text",
                                                ),
                                                html.Small(
                                                    "LinkedIn Profile",
                                                    className="card-text text-muted",
                                                ),
                                            ]
                                        ),
                                        className="col-md-8",
                                    ),
                                ],
                                className="g-0 d-flex align-items-center",
                            )
                        ],                                  
                className="mb-3",
                style={"maxWidth": "540px"},
            ),

            dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                src="/assets/imgs/strange.jpg",
                                className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4("Dr. Strange", className="card-title"),
                                    html.P(
                                        "This is a wider card with supporting text "
                                        "below as a natural lead-in to additional "
                                        "content. This content is a bit longer.",
                                        className="card-text",
                                    ),
                                    html.Small(
                                        "LinkedIn Profile",
                                        className="card-text text-muted",
                                    ),
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],                                  
    className="mb-3",
    style={"maxWidth": "540px"},
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