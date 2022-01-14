# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import os
import glob

# # df for testing app
# df = pd.DataFrame({
#     "Individual": ["Mike Musty", "Nicole Labrecque", "Alison Tavel", "Mike Musty", "Nicole Labrecque", "Alison Tavel"],
#     "Score": [90, 100, 82, 82, 90, 100],
#     "Race": ["Shamrock Shuffle", "Shamrock Shuffle", "Shamrock Shuffle", "Sprouty", "Sprouty", "Sprouty"],
#     "Age Group": ["M3039", "F3039", "F3039", "M3039", "F3039", "F3039"]
# })


# read latest table from output_data/tables/
path = os.path.abspath("output_data/tables/")  # absolute path without / at the end
list_of_filenames = glob.glob(f"{path}/*")
df = pd.read_csv(max(list_of_filenames, key=os.path.getctime))
df.sort_values(by=['Race'], inplace=True)

# TODO: filter df to only include top N scores for an individual

available_indicators = df["Age Group"].unique()

app = dash.Dash(__name__)
app.title = "2021 UVRS Scorecard"
server = app.server

app.layout = html.Div([
    html.H1("2021 Upper Valley Running Series Scorecard"),
    html.Div("Select Age Group"),
    html.Div(
        dcc.Dropdown(
            id="age-group",
            options=[{'label': i, 'value': i} for i in available_indicators],
            value="Age Group"
        ), style={'width': '20%'}),
    dcc.Graph(id="main_graph")
])

@app.callback(
    Output("main_graph", "figure"),
    Input("age-group", "value")
)
def update_graph(age_group):
    dff = df[df["Age Group"] == age_group]
    fig = px.bar(dff, y="Individual", x="Score", color="Race", orientation="h", barmode="stack")
    fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

