# AI Assistance
## Google Gemini asked how to code fetch_disability_fact function using random package,
## after prompting for how to create a function iterating through facts_list to choose a random index value to print
from dash import html, register_page, dcc, Input, Output, callback
import requests
import random

register_page(__name__, path="/fun-fact", name="Fun Fact")

layout = html.Div([
    html.H2("Did You Know?", style={"color": "white", "textAlign": "center", "marginTop": "20px"}),
    html.Button(
        "Click for a fact about disabilities/accessibility",
        id="button-fact",
        n_clicks=0,
        style={
            "backgroundColor": "white",
            "color": "black",
            "border": "none",
            "borderRadius": "8px",
            "padding": "14px 28px",
            "margin": "16px 0",
            "fontSize": "1.2em",
            "fontWeight": "bold",
            "cursor": "pointer",
            "transition": "background 0.2s, color 0.2s"
        },
        className="fact-btn"
    ),
    dcc.Loading(html.Div(id="disability-fact", style={"color": "white", "fontSize": "1.2em", "margin": "16px 0"})),
    html.P("See more facts: ", style={"color": "white", "marginTop": "24px"}),
    html.A("Fun facts source", href="https://facts.net/society-and-social-sciences/society/32-facts-about-disability/", 
           style={"color": "white", "textDecoration": "underline"},
           target="_blank"),
], style={
    "backgroundColor": "#16213e",
    "padding": "36px 32px 32px 32px",
    "borderRadius": "8px",
    "boxShadow": "0 2px 8px rgba(30,58,138,0.10)",
    "maxWidth": "900px",
    "margin": "32px auto"
})

facts_list = ["Over 1 billion people, about 15 percent of the world's population, live with some form of disability.","Disabilities can be congenital (present at birth) or acquired later in life due to illness, injury, or aging.","The World Health Organization (WHO) states that disability is not just a health problem but a complex phenomenon reflecting the interaction between features of a person’s body and society.","The Americans with Disabilities Act (ADA) was signed into law in 1990 to protect the rights of people with disabilities in the U.S.","The International Day of Persons with Disabilities is observed on December 3rd each year to promote the rights and well-being of persons with disabilities.","Physical disabilities affect a person’s mobility or dexterity. Examples include spinal cord injuries, cerebral palsy, and muscular dystrophy.","Universal design is a concept that aims to create products and environments accessible to all people, regardless of disability.","Braille is a tactile writing system used by people who are visually impaired. It was invented by Louis Braille in 1824.","Assistive technology includes devices like wheelchairs, hearing aids, and screen readers that help people with disabilities perform daily tasks.","Sign language is a visual language used by the deaf community. American Sign Language (ASL) is widely used in the United States."]

@callback(
    Output("disability-fact", "children"),
    Input("button-fact", "n_clicks")
)

def fetch_disability_fact(n):
    if n > 0:
        random_fact = random.choice(facts_list)
        return random_fact
    # Return an empty string on initial page load
    return ""

