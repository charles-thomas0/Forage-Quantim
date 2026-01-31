# tests/test_app_layout.py
import pytest
from dash import Dash
from src.components.layout import create_layout

@pytest.fixture
def dash_app(dash_duo):
    """
    Initialize the Dash app and return the dash_duo fixture
    so we can interact with it in tests.
    """
    app = Dash()
    app.title = "Sales Price Increase"
    app.layout = create_layout(app)

    # Start the app
    dash_duo.start_server(app)
    return dash_duo

def test_header_is_present(dash_app):
    """Test that the main header (H1) is present on screen."""
    dash_duo = dash_app
    # Wait until header is visible in the DOM
    dash_duo.wait_for_element("h1")
    header = dash_duo.find_element("h1")
    assert header is not None
    # Basic text check (should at least contain 'Sales' or your title text)
    assert "Sales" in header.text

def test_graph_is_present(dash_app):
    """Test that the graph component is present."""
    dash_duo = dash_app
    # The Graph has id="sales-line-graph"
    dash_duo.wait_for_element("#sales-line-graph")
    graph = dash_duo.find_element("#sales-line-graph")
    assert graph is not None

def test_region_picker_is_present(dash_app):
    """Test that the radio button region picker is present."""
    dash_duo = dash_app
    # The region picker has id="region-selector"
    dash_duo.wait_for_element("#region-selector")
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None
