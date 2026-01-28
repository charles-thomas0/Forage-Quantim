# main.py
from dash import Dash
import dash_bootstrap_components as dbc
from src.components.layout import create_layout

def main() -> None:
    # Use BOOTSTRAP theme for professional styling
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Sales Price Increase"
    app.layout = create_layout(app)
    app.run_server(debug=True)  # debug=True for easier development

if __name__ == "__main__":
    main()
