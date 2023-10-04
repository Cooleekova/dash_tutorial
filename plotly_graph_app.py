# Import packages

# We import the dcc module (DCC stands for Dash Core Components). 
# This module includes a Graph component called dcc.Graph, which is used to render interactive graphs.

from dash import Dash, html, dash_table, dcc
import pandas as pd

# We also import the plotly.express library to build the interactive graphs.
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    # Using the plotly.express library, we build the histogram chart 
    # and assign it to the figure property of the dcc.Graph. 
    # This displays the histogram in our app.
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
