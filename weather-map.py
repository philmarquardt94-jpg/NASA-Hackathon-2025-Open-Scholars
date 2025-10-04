import pydeck as pdk
import pandas as pd

# City data
data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Albuquerque'],
    'latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 35.106766],
    'longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740, -106.629181],
}

df = pd.DataFrame(data)

# Define the scatterplot layer
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[longitude, latitude]',
    get_fill_color='[0, 128, 255, 180]',
    get_radius=40000,
    pickable=True,
)

# World view
view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1.5)

# Tooltip (shows city name)
tooltip = {"html": "<b>City:</b> {city}", "style": {"color": "white"}}

# Create map
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip,
    map_style='https://basemaps.cartocdn.com/gl/positron-gl-style/style.json',
)

# Save to HTML
deck.to_html("weather_map.html", open_browser=False)
print("weather_map.html created!")
