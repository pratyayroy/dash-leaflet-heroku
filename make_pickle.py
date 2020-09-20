import json
import pickle
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx
import pandas as pd
import numpy as np

from dash.dependencies import Output, Input

df = pd.read_csv('gridcities.csv')
color_prop = 'population'

df_state = df.dropna()
df_state = df_state[['lat', 'lng', 'city', 'population', 'density']]  # drop irrelevant columns
dicts = df_state.to_dict('rows')
for item in dicts:
    item["tooltip"] = item["city"]  # bind tooltip
    
geojson = dlx.dicts_to_geojson(dicts, lon="lng")  # convert to geojson
geobuf = dlx.geojson_to_geobuf(geojson)  # convert to geobuf

with open('geobuf.pkl', 'wb') as f:
    pickle.dump(geobuf, f, pickle.HIGHEST_PROTOCOL)

geojson = dl.GeoJSON(data=geobuf, id="geojson", format="geobuf",
                     zoomToBounds=True,  # when true, zooms to bounds when data changes
                     cluster=True,  # when true, data are clustered
                     clusterToLayer=dlx.scatter.cluster_to_layer,  # how to draw clusters
                     zoomToBoundsOnClick=True,  # when true, zooms to bounds of feature (e.g. cluster) on click
                     options=dict(pointToLayer=dlx.scatter.point_to_layer),  # how to draw points
                     superClusterOptions=dict(radius=150),
                     hideout={'colorscale': ['green'], 'color_prop': color_prop, 'min': 0, 'max': 0})

with open('geojson.pkl', 'wb') as g:
    pickle.dump(geojson, g, pickle.HIGHEST_PROTOCOL)