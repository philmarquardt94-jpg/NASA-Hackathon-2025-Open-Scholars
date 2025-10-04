import pydeck as pdk
import pandas as pd

# Sample data: City emissions data
data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Albuquerque'],
    'latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 35.106766],
    'longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740, -106.629181],
    'ch4_emissions': [250, 180, 210, 230, 160, 180],  # Sample CH4 emissions data
    'co2_emissions': [5000, 4300, 3800, 4500, 3200, 2900]  # Sample CO2 emissions data
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define the deck.gl layer
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[longitude, latitude]',
    get_fill_color='[255, 0, 0, 160]',  # Red color with transparency
    get_radius='ch4_emissions',  # Use CH4 emissions as the radius
    radius_scale=100,
    pickable=True,
)

# Set the view for the initial map
view_state = pdk.ViewState(
    latitude=37.0902,  # Center of the US
    longitude=-95.7129,
    zoom=4,
    pitch=0,
)

# Create the deck.gl map
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "html": "<b>City:</b> {city}<br/><b>CH4 Emissions:</b> {ch4_emissions} kg<br/><b>CO2 Emissions:</b> {co2_emissions} kg",
        "style": {"color": "white"},
    },
)

# Render the map
deck.to_html("emissions_map.html")  # Save the map as an HTML file
