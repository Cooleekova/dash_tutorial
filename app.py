# When creating Dash apps, you will almost always use the import statement above. 
# As you create more advanced Dash apps, you will import more packages.
from dash import Dash, html

# This line is known as the Dash constructor and is responsible for initializing your app. 
# It is almost always the same for any Dash app you create.
app = Dash(__name__)

# The app layout represents the app components that will be displayed in the web browser, 
# normally contained within a html.Div.
app.layout = html.Div([
    html.Div(children='Hello World'),
])

# These lines are for running your app, 
# and they are almost always the same for any Dash app you create.
if __name__ == '__main__':
    app.run(debug=True)