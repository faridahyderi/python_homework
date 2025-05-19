from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the built-in gapminder dataset
df = px.data.gapminder()

# Get unique country names
countries = df['country'].unique()

# Initialize the Dash app
app = Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    html.H1("GDP per Capita Over Time"),
    
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"  # Default selected country
    ),
    
    dcc.Graph(id="gdp-growth")
])

# Callback to update the graph based on selected country
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita Over Time: {selected_country}"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
