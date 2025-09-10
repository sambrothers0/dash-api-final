AI Disclaimer: AI was used to format most of this text into markdown format, although the text itself was mostly human made

## 50 States Accessibility Guide

**A website for mapping and displaying accessibility-related information, organized by US state.**

Created by **Group 8** for Professor Schlosser's *Competing Through Business Analytics* class at **William & Mary** in the Master's of Business Analytics program during **Fall 2025**.

The site is deployed live on Render: [Live Site](https://dash-api-final.onrender.com)

---

## Project Overview

The problem our website seeks to address is the gap in availability of travel information on accessibility. Our goal is to fill this gap with an informative and visually compelling webpage that provides rich accessibility data from live APIs. We've chosen to focus on all US states to be as comprehensive as possible, while still keeping our topic narrow and focused.

**Audience:** Domestic and international tourists, especially those with a physical disability.

We have also included a collection of disability advocacy groups for getting directly involved with the disabled community.

**Value:** This project provides a helpful place for people who are concerned with accessibility to find travel information across the states.

---

## Technology

The website is created using **Python's Dash** package for single page web applications and **Plotly** for visualization.

---

## Running and Deployment

Although the project is deployed live on Render, it can easily be run locally:

1. Install a recent version of Python.
2. Install the packages listed in `requirements.txt` using a Python installer such as `pip`.
3. After dependencies have been installed, run `app.py` from the root directory.

---

## Data Sources

Breedlove, N. (2025). The best and worst U.S. states for people with disabilities. AAA State of 
Play.  https://www.aaastateofplay.com/the-best-and-worst-us-states-for-people-with-
disabilities/​


Disability Resources. (2025). In Disability Resources, Inc. https://www.disabilityresources.org/​


Pineda, T. (2025, March 10). 32 facts about disability. Facts.net. 
https://facts.net/society-and-social-sciences/society/32-facts-about-disability/ ​


Thomas, N., Bach, S., & Houtenville, A. (2025). Annual Disability Statistics Compendium: 2025. University of New Hampshire, Institute on Disability. 
https://www.researchondisability.org/annual-disability-statistics-collection/2025-compen
dium-table-contents

---

## Data Dictionary

**Overview**

| Column Name | Description | Type    | Units |
|-------------|-------------|---------|-------|
| State       | Two-letter abbreviation of the US state. Identifies the state on the map. | Text    | N/A   |
| Points      | Aggregate disability friendliness score for the state. Higher points indicate a more disability-friendly state. | Numeric | Points |
| Rank        | Rank of the state based on the disability friendliness score. Lower rank = better accessibility. | Numeric | Rank   |

**Details Page**

| Column Name | Description | Type    | Units |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------|-------------------------------|
| Disabled Individuals | Number of individuals with any disability living in the community in the state. | Numeric | People |
| HEARING Disabled Individuals | Number of individuals with a hearing disability in the state. | Numeric | People |
| VISION Disabled Individuals | Number of individuals with a vision disability in the state. | Numeric | People |
| COGNITIVE Disabled Individuals | Number of individuals with a cognitive disability in the state. | Numeric | People |
| Disabled Individuals Ages 18-64 Employed | Number of disabled individuals aged 18-64 who are employed. | Numeric | People |
| HEARING Disabled Individuals Ages 18-64 Employed | Number of hearing-disabled individuals aged 18-64 who are employed. | Numeric | People |
| VISION Disabled Individuals Ages 18-64 Employed | Number of vision-disabled individuals aged 18-64 who are employed. | Numeric | People |
| COGNITIVE Disabled Individuals Ages 18-64 Employed | Number of cognitive-disabled individuals aged 18-64 who are employed. | Numeric | People |
| Median Wage for Disabled Workers | Annual median earnings for full-time disabled workers. | Numeric | $ |
| Healthcare Insurance Coverage Rate for Disabled Individuals | Percentage of disabled individuals with health insurance coverage. | Numeric | % of people by state population |
| Percentage of Disabled Individuals With a HighSchool Degree | Percentage of disabled individuals who have completed a high school degree. | Numeric | % of people by state population |
| Percentage of Disabled Individuals With a 4-Year College Degree | Percentage of disabled individuals who have completed a 4-year college degree. | Numeric | % of people by state population |
| Disabled Individuals (% of population) | Disabled Individuals as a percentage of the total state population. | Numeric | % of people by state population |
| HEARING Disabled Individuals (% of population) | Hearing-disabled individuals as a percentage of the total state population. | Numeric | % of people by state population |
| VISION Disabled Individuals (% of population) | Vision-disabled individuals as a percentage of the total state population. | Numeric | % of people by state population |
| COGNITIVE Disabled Individuals (% of population) | Cognitive-disabled individuals as a percentage of the total state population. | Numeric | % of people by state population |
| Disabled Individuals Ages 18-64 Employed (% of population) | Employed disabled individuals aged 18-64 as a percentage of total state population. | Numeric | % of people by state population |
| HEARING Disabled Individuals Ages 18-64 Employed (% of population) | Employed hearing-disabled individuals aged 18-64 as a percentage of total state population. | Numeric | % of people by state population |
| VISION Disabled Individuals Ages 18-64 Employed (% of population) | Employed vision-disabled individuals aged 18-64 as a percentage of total state population. | Numeric | % of people by state population |
| COGNITIVE Disabled Individuals Ages 18-64 Employed (% of population) | Employed cognitive-disabled individuals aged 18-64 as a percentage of total state population. | Numeric | % of people by state population |

**Resources**

| Field           | Description                                                                                          | Type                   | Notes |
|-----------------|------------------------------------------------------------------------------------------------------|------------------------|-------|
| state_choice    | The US state selected by the user from the dropdown. Determines which state’s disability resources are displayed. | Text                   | N/A   |
| url             | The URL of the state-specific page on disabilityresources.org to scrape resources from.              | Text                   | N/A   |
| resource_links  | List of `<a>` tags extracted from the web page containing links to state disability resources.        | List of HTML elements  | N/A   |
| link_url        | URL of an individual disability resource link. Extracted from `resource_links`.                      | Text                   | URL   |
| link_text       | Display text of an individual disability resource link. Extracted from `resource_links`.             | Text                   | N/A   |


**Fun Fact**

| Field           | Description                                                                 | Type              | Notes |
|-----------------|-----------------------------------------------------------------------------|-------------------|-------|
| facts_list      | List of pre-defined fun facts about disabilities and accessibility. Randomly displayed when the user clicks the button. | List of Text      | N/A   |
| n_clicks        | Number of times the “Click for a fact” button has been pressed. Used to trigger the callback. | Numeric           | Count |
| random_fact     | A single fact randomly selected from `facts_list` to display on the page.   | Text              | N/A   |
| disability-fact | HTML Div where the randomly selected fact is displayed. Updated dynamically via callback. | HTML Element      | N/A   |
| button-fact     | Button that the user clicks to see a new fact.                              | HTML Element      | N/A   |


---

### Developers

Ashley Gasswint  
Pooja Muthuraj  
Alex Farina  
Sam Brothers

Initial code based on work by Dr. Pamela Schlosser
