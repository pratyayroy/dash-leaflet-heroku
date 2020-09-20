import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import pickle

# region Data
color_prop = 'population'

def get_data_pkl():
    with open('geojson.pkl', 'rb') as f:
        geojson = pickle.load(f)
    return geojson

# Create the app
chroma = "https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js"
tile_url = "https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png" # http://leaflet-extras.github.io/leaflet-providers/preview/
app = dash.Dash(external_scripts=[chroma], prevent_initial_callbacks=True)
app.title = 'AC Dashboard'
app.layout = html.Div([
    dl.Map([dl.TileLayer(url=tile_url), get_data_pkl()])
], style={'width': '100%', 'height': '95vh', 'margin': "auto", "display": "block", "position": "relative"})
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
