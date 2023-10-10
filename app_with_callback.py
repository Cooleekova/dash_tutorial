# Import packages

# To work with the callback in a Dash app, 
# we import the callback module and the two arguments 
# commonly used within the callback: Output and Input.

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
    # Both the RadioItems and the Graph components were given id names: 
    # these will be used by the callback to identify the components.
])

# Add controls to build the interaction

# The inputs and outputs of our app are the properties of a particular component. 
# In this example, our input is the value property of the component that has the ID "controls-and-radio-item". 
# If you look back at the layout, you will see that this is currently lifeExp. 
# Our output is the figure property of the component with the ID "controls-and-graph", 
# which is currently an empty dictionary (empty graph).

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    # The callback function's argument col_chosen refers to the component property of the input lifeExp. 
    # We build the histogram chart inside the callback function, assigning the chosen radio item to the y-axis attribute of the histogram. 
    # This means that every time the user selects a new radio item, the figure is rebuilt and the y-axis of the figure is updated.
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig
    # Finally, we return the histogram at the end of the function. 
    # This assigns the histogram to the figure property of the dcc.Graph, thus displaying the figure in the app.


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
