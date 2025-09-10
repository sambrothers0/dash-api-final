#AI Usage: CoPilot and ChatGPT used in sections: Convert state names to 2-letter codes, Decide formatting for hover + colorbar and Set hovertemplate
from dash import html, dcc, Input, Output, callback, register_page, dash_table
import pandas as pd
import plotly.express as px
from pathlib import Path
import us 

register_page(__name__, path="/details", name="Disability Info by State")


# Load CSV
Data_Path = Path(__file__).resolve().parent.parent / "data" / "disabilities.csv"
df = pd.read_csv(Data_Path)


# Convert state names to 2-letter codes
df['state_code'] = df['State'].apply(lambda x: us.states.lookup(x).abbr if us.states.lookup(x) else None)


# Rename columns
df.rename(columns={
    "# with Disability Living in the Community": "Disabled Individuals",
    "# with Hearing Disability": "HEARING Disabled Individuals",
    "#with Vision Disability": "VISION Disabled Individuals",
    "# with Cognitive Disability": "COGNITIVE Disabled Individuals",
    "# with disability Ages 18-64 Employed": "Disabled Individuals Ages 18-64 Employed",
    "# ages 18-64 Employed with Hearing Dis": "HEARING Disabled Individuals Ages 18-64 Employed",
    "# Ages 18-64 Employed  with Vision Dis": "VISION Disabled Individuals Ages 18-64 Employed",
    "# Ages 18-64 Employed with Cognitive Dis": "COGNITIVE Disabled Individuals Ages 18-64 Employed",
    "$Annual Median Earnings Full-Time with Disability": "Median Wage for Disabled Workers",
    "% Health Insurance Coverage Rate for Disabled Individuals": "Healthcare Insurance Coverage Rate for Disabled Individuals",
    "% Disabled Individuals With HighSchool Degree": "Percentage of Disabled Individuals With a HighSchool Degree",
    "% Disabled Individuals With 4-Year College Degree": "Percentage of Disabled Individuals With a 4-Year College Degree"
}, inplace=True)

# Normalize selected columns by population and fix percentage issues
df["Disabled Individuals (% of population)"] = df["Disabled Individuals"] / df["2023-Population"] * 100
df["HEARING Disabled Individuals (% of population)"] = df["HEARING Disabled Individuals"] / df["2023-Population"] * 100
df["VISION Disabled Individuals (% of population)"] = df["VISION Disabled Individuals"] / df["2023-Population"] * 100
df["COGNITIVE Disabled Individuals (% of population)"] = df["COGNITIVE Disabled Individuals"] / df["2023-Population"] * 100
df["Disabled Individuals Ages 18-64 Employed (% of population)"] = df["Disabled Individuals Ages 18-64 Employed"] / df["2023-Population"] * 100
df["HEARING Disabled Individuals Ages 18-64 Employed (% of population)"] = df["HEARING Disabled Individuals Ages 18-64 Employed"] / df["2023-Population"] * 100
df["VISION Disabled Individuals Ages 18-64 Employed (% of population)"] = df["VISION Disabled Individuals Ages 18-64 Employed"] / df["2023-Population"] * 100
df["COGNITIVE Disabled Individuals Ages 18-64 Employed (% of population)"] = df["COGNITIVE Disabled Individuals Ages 18-64 Employed"] / df["2023-Population"] * 100
df["Percentage of Disabled Individuals With a HighSchool Degree"] *= 100
df["Percentage of Disabled Individuals With a 4-Year College Degree"] *= 100
df["Healthcare Insurance Coverage Rate for Disabled Individuals"] *= 100

# Dropdown options
numeric_columns = [
    "Disabled Individuals (% of population)",
    "HEARING Disabled Individuals (% of population)",
    "VISION Disabled Individuals (% of population)",
    "COGNITIVE Disabled Individuals (% of population)",
    "Disabled Individuals Ages 18-64 Employed (% of population)",
    "HEARING Disabled Individuals Ages 18-64 Employed (% of population)",
    "VISION Disabled Individuals Ages 18-64 Employed (% of population)",
    "COGNITIVE Disabled Individuals Ages 18-64 Employed (% of population)",
    "Median Wage for Disabled Workers",
    "Healthcare Insurance Coverage Rate for Disabled Individuals",
    "Percentage of Disabled Individuals With a HighSchool Degree",
    "Percentage of Disabled Individuals With a 4-Year College Degree"
]


# Layout
layout = html.Div(
    style={"backgroundColor": "rgba(0,0,0,0)", "color": "white", "padding": "10px"},
    children=[
        html.H1("US Disability Data by State", style={"color": "#cdd6d3", "textAlign": "center"}),

        html.Div(
            [
                html.Label("Select Column to Display:", style={"marginBottom": "8px"}),
                dcc.Dropdown(
                    id="column-dropdown",
                    options=[{"label": col, "value": col} for col in numeric_columns],
                    value=numeric_columns[0],
                    clearable=False,
                    style={"color": "black"}
                ),
            ],
            style={"width": "40%", "margin": "0 auto"}  # Center the dropdown
        ),

        html.Br(),

        # Graph for choropleth
        dcc.Graph(id="choropleth-map"),

        html.H2("Top & Bottom 5 States", style={"color": "white", "textAlign": "center", "marginTop": "20px"}),

        # Table
        dash_table.DataTable(
            id="top-bottom-table",
            style_header={
                'backgroundColor': '#16213e',
                'color': 'white',
                'fontWeight': 'bold'
            },
            style_cell={
                'backgroundColor': '#16213e',
                'color': 'white',
                'textAlign': 'left',
                'padding': '5px'
            },
            style_table={'margin': '0 auto', 'width': '60%'}  # Center the table
        )
    ]
)

@callback(
    Output("choropleth-map", "figure"),
    Input("column-dropdown", "value")
)
def update_map(selected_column):
    # Get the color values
    color_values = df[selected_column]

    fig = px.choropleth(
        df,
        locations="state_code",
        locationmode="USA-states",
        color=color_values,
        color_continuous_scale="Cividis",
        scope="usa",
        labels={selected_column: selected_column}
    )

    # Decide formatting for hover and colorbar
    if "(% of population)" in selected_column or "Percentage" in selected_column or "Rate" in selected_column:
        value_format = "%{z:.2f}%"     # 2 decimals
        tick_format = ".2f"            # 2 decimals
        suffix = "%"
    elif "Wage" in selected_column or "Earnings" in selected_column or "Median" in selected_column:
        value_format = "$%{z:,.0f}"
        tick_format = "$,.0f"
        suffix = ""
    else:
        value_format = "%{z:,}"
        tick_format = ",.0f"
        suffix = ""

    # Set hovertemplate
    fig.update_traces(
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            f"{selected_column}: {value_format}"
            "<extra></extra>"
        ),
        customdata=df[["State"]]
    )

    # Set colorbar formatting
    fig.update_coloraxes(
        colorbar=dict(
            title=selected_column,
            tickformat=tick_format,
            ticksuffix=suffix
        )
    )

    fig.update_layout(
        geo=dict(bgcolor="#0a2342"),
        paper_bgcolor="#0a2342", 
        plot_bgcolor="#0a2342",   
        font_color="white",
        margin=dict(l=10, r=10, t=50, b=10)
    )

    return fig

# Table Callback

@callback(
    Output("top-bottom-table", "data"),
    Output("top-bottom-table", "columns"),
    Input("column-dropdown", "value")
)
def update_table(selected_column):
    # Sort descending for top 5
    sorted_df = df.sort_values(by=selected_column, ascending=False)
    top5 = sorted_df.iloc[:5, :][["State", selected_column]]
    bottom5 = sorted_df.iloc[-5:, :][["State", selected_column]]

    # Put in a separator row
    separator = pd.DataFrame([{"State": "Top 5 ↑ ----- Bottom 5 ↓", selected_column: None}])

    # Put top5 + separator + bottom5 into table
    table_df = pd.concat([top5, separator, bottom5]).reset_index(drop=True)

    table_data = table_df.to_dict('records')
    table_columns = [{"name": col, "id": col} for col in table_df.columns]

    return table_data, table_columns

#Looking at data on different aspects of disability across US states!
#This map shows users various statistics related to disabilities in each state, such as:
#       the percentage of individuals with disabilities, employment rates among disabled individuals, 
#       median wages, healthcare coverage rates, and levels of education.


#How to use:
# 1. Select a column from the dropdown menu to visualize different aspects of disability data across US states.
# 2. Hover over a state on the map to see detailed information about that state, including the selected metric.
# 3. The color intensity on the map represents the value of the selected metric, with a color bar indicating the scale.
