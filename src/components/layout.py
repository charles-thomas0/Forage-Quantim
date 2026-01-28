# src/components/layout.py
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

def create_layout(app: Dash) -> html.Div:
    # Load your data
    df = pd.read_csv("/home/charlest/Programming/Forage-Quantim/data/output.csv")

    # Create professional line chart
    fig = px.line(
        df,
        x="date",
        y="sales",
        title="Change in Sales from Price Increase",
        markers=True
    )

    # Update layout for style
    fig.update_layout(
        title_font_size=24,
        title_font_family="Arial",
        xaxis_title="Date",
        yaxis_title="Sales (£)",
        xaxis=dict(
            showgrid=True,
            gridcolor="lightgrey",
            tickangle=-45,
            showline=True,
            linewidth=1,
            linecolor="black",
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="lightgrey",
            showline=True,
            linewidth=1,
            linecolor="black",
        ),
        plot_bgcolor="white",
        margin=dict(l=40, r=20, t=60, b=40),
        font=dict(family="Arial", size=12, color="black"),
    )

    # Update traces for markers & hover
    fig.update_traces(
        line=dict(color="royalblue", width=3),
        marker=dict(size=6),
        hovertemplate="Date: %{x}<br>Sales: £%{y:.2f}"
    )

    # Dash layout using Bootstrap
    layout = dbc.Container(
        fluid=True,
        children=[
            dbc.Row(
                dbc.Col(html.H1(app.title, className="text-center mt-4 mb-2"), width=12)
            ),
            dbc.Row(
                dbc.Col(html.H5(
                    "Visualizing how sales changed with price increases",
                    className="text-center mb-4"
                ), width=12)
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="sales-line-graph",
                                figure=fig,
                                config={'displayModeBar': True}  # Show zoom/save toolbar
                            )
                        ),
                        className="shadow-sm mb-4"
                    ),
                    width=12
                )
            ),
        ]
    )

    return layout
