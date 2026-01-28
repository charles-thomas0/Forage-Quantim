from dash import html, dcc, Dash, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

REGION_COLORS = {
    "north": "#4FC3F7",
    "east": "#9575CD",
    "south": "#81C784",
    "west": "#FFB74D",
}

def create_layout(app: Dash) -> html.Div:
    df = pd.read_csv("/home/charlest/Programming/Forage-Quantim/data/output.csv")
    df["region"] = df["region"].str.lower()

    fig = px.line(
        df,
        x="date",
        y="sales",
        color="region",
        color_discrete_map=REGION_COLORS,
        markers=True,
        title="Sales Impact Following Price Adjustment"
    )

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="#0E1117",
        paper_bgcolor="#0E1117",
        title_font_size=22,
        font=dict(color="#E6E8EB", family="Inter, Arial"),
        margin=dict(l=40, r=20, t=70, b=40),
        xaxis=dict(
            title="Date",
            tickangle=-45,
            showgrid=True,
            gridcolor="rgba(255,255,255,0.04)",
            zeroline=False
        ),
        yaxis=dict(
            title="Sales (£)",
            showgrid=True,
            gridcolor="rgba(255,255,255,0.04)",
            zeroline=False
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=5),
        hovertemplate="%{x}<br><b>£%{y:.2f}</b><extra></extra>"
    )

    layout = dbc.Container(
        fluid=True,
        style={
            "backgroundColor": "#0E1117",
            "minHeight": "100vh",
            "padding": "48px"
        },
        children=[
            dbc.Row(
                dbc.Col(
                    html.Div([
                        html.H1(
                            "Pink Morsels — Regional Sales",
                            style={
                                "fontWeight": "500",
                                "letterSpacing": "-0.5px",
                                "marginBottom": "4px"
                            }
                        ),
                        html.P(
                            "Post-price-increase performance by region",
                            style={"color": "#9AA0A6"}
                        )
                    ])
                )
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        dcc.RadioItems(
                            id="region-selector",
                            options=[
                                {"label": "All Regions", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            labelStyle={
                                "marginRight": "24px",
                                "cursor": "pointer",
                                "color": "#C9CDD2",
                                "fontSize": "14px"
                            },
                            inputStyle={"marginRight": "6px"}
                        ),
                        style={
                            "marginTop": "24px",
                            "marginBottom": "24px"
                        }
                    )
                )
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="sales-line-graph",
                                figure=fig,
                                config={"displayModeBar": False}
                            )
                        ),
                        style={
                            "backgroundColor": "#11151C",
                            "border": "1px solid rgba(255,255,255,0.06)",
                            "borderRadius": "10px"
                        }
                    )
                )
            )
        ]
    )

    @app.callback(
        Output("sales-line-graph", "figure"),
        Input("region-selector", "value")
    )
    def update_graph(region):
        filtered_df = df if region == "all" else df[df["region"] == region]

        fig = px.line(
            filtered_df,
            x="date",
            y="sales",
            color="region" if region == "all" else None,
            color_discrete_map=REGION_COLORS,
            markers=True,
            title="Sales Impact Following Price Adjustment"
        )

        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor="#0E1117",
            paper_bgcolor="#0E1117",
            font=dict(color="#E6E8EB"),
            xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.04)", tickangle=-45),
            yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.04)")
        )

        fig.update_traces(
            line=dict(
                width=3,
                color=REGION_COLORS.get(region)
            ),
            marker=dict(size=6),
            hovertemplate="%{x}<br><b>£%{y:.2f}</b><extra></extra>"
        )

        return fig

    return layout
