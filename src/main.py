from dash import Dash
import dash_bootstrap_components as dbc
from src.components.layout import create_layout

def main() -> None:
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Sales Price Increase"

    # Pass the app to layout so callbacks work
    app.layout = create_layout(app)

    app.run(debug=True)  # debug=True for development

if __name__ == "__main__":
    main()
