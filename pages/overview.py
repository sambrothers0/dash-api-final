#AI usage comment: Copilot was used to help put this page together. It was used to help with formatting, debugging, and was used to quickly update the DisabilityRankedStates.csv from full state names to abreviations.
import dash
from dash import Dash, html, dcc, Input, Output, callback, page_container
from pathlib import Path
import pandas as pd
import plotly.express as px


dash.register_page(__name__, path="/", name="Map")

#Load the dataset
Data_Path = Path(__file__).resolve().parent.parent / "data" / "DisabilityRankedStates.csv"
df = pd.read_csv(Data_Path)


#Chloropleth map
fig = px.choropleth(
    df,
    locations = "State",
    locationmode= "USA-states",
    color = "Points",
    scope= "usa",
    labels = {"Points": "Disability Friendly Rank"},
    color_continuous_scale= "Cividis",
    range_color= (0, 225),
    hover_data=["Rank"]
)

fig.update_layout(
    title_text="Disability Friendliness by State",
    geo=dict(showlakes=True, lakecolor="lightblue"),
    paper_bgcolor="#0a2342",  
    plot_bgcolor="#0a2342",  
    font_color="white",
    margin={"r":0,"t":40, "l":0, "b":0}
)

layout = html.Div([
    html.Div([
        html.H3("Mapping Accessibility Through Aggregated Scores", className="map-header"),
        html.P(
            "This interactive map displays the disability friendliness of each US state, ranked numerically by points. "
            "The ranking is aggregated from scores on various factors such as housing, healthcare, employment opportunities, "
            "and social inclusion for people with disabilities. Data is sourced from AAA State of Play rankings.",
            className="map-subtitle"
        ),
    ], className="resources-page-wrapper"),
    html.Div([
        dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"padding": "24px"}),
    ], className="page1-grid"),
    html.Div([
        html.H2("How to Use This Map", className="landing-header"),
        html.P(
            "Hover over each state to see its accessibility score. States with higher scores are more disability-friendly. "
            "Use this map to compare states and find accessible places to live, work, or travel.",
            className="landing-subtitle"
        ),
    ], className="page-wrapper"),
])
