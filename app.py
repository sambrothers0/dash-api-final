# AI use statement: AI was used minimally within this page. Its main purpose was to write and explain certain code that the developers were less familiar with, such as alternative text on images. AI was also responsible for naming many of the classes within this file.
import dash
from dash import Dash, html, dcc, Input, Output, callback, page_container
import dash_bootstrap_components as dbc

#initialize the app
app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, title="50 States Accessibility Guide")

server = app.server #for deployment

app.layout = html.Div([
    # Main page container with border
    html.Div([
    html.Div([
        html.H1("50 States Accessibility Guide", className="app-title"),
        html.Img(src="/assets/img/logo.png", className="header-logo", alt="Project logo"),
    ], className="header-bar"),
    html.Div([
        html.Img(src="/assets/img/Disability_Symbols_Blog.webp", 
                 className="landing-image", alt="3 blue disability symbols"),
    ], className="image-banner"),
    html.H2("A guide to help you find accessible places in the US", className="landing-header"),
    html.H3("The problem our website seeks to address is the gap in availability of travel"
            " information on accessibility. Our goal is to fill this gap with an informative"
            " and visually compelling webpage that provides rich accessibility data from real"
            " web sources. We've chosen to focus on all US states to be as comprehensive as"
            " possible, while still keeping our topic narrow and focused.", className="landing-subtitle"),
    html.H2("Take a look around", className="landing-header"),
    html.H3("Our website includes several features which make it easier for users to view "
            "and understand accessibility data. There is an interactive map that displays "
            " accessibility ratings for each state, allowing users to quickly identify"
            " areas with high or low accessibility. The details page features more comprehensive"
            " disability data based on various categories of disability. We have also"
            " included a collection of disability advocacy groups for getting directly involved"
            " with the disabled community. This project provides a helpful place for people"
            " who are concerned with accessibility to find travel information across the states,"
            " whether or not you are American.", className="landing-subtitle"),
    dbc.Navbar(
        dbc.Container([
            dbc.Nav(
                [
                    dbc.NavLink("Overview", href="/", active="exact"),
                    dbc.NavLink("Details", href="/details", active="exact"),
                    dbc.NavLink("Resources", href="/resources", active="exact"),
                    dbc.NavLink("Fun Fact", href="/fun-fact", active="exact")
                ],
                className="custom-navbar"
            ),
        ]),
        color="light",
        dark=False,
        className="mb-4"
    ),
    html.Div(page_container, className="nav-page-border"),
    html.H2("Conscious Design", className="landing-footer"),
    html.H3("In creating this website, we have made a conscious effort to ensure"
            " that it is accessible to all users, including those with disabilities."
            " We have used high-contrast colors and large fonts to make the text"
            " easy to read, and we have ensured that all images have alt text for screen readers."
            " We hope that our website may lead by example and further assist in"
            " promoting accessibility through not only the information it contains,"
            " but also the way that information is presented.", className="footer-subtitle"),
    html.A("Project Information and Code", href="https://github.com/sambrothers0/dash-api-final", target="_blank", className="footer-link")
    ]),
])

if __name__ == "__main__":
    app.run(debug=True)
