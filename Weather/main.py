#@title Plot weather data
import pandas as pd
import plotly.graph_objects as go

# Sample DataFrame: Replace 'df' with your weather data DataFrame
df = pd.read_csv('5_day_weather_data.csv')

# Adding a 'Day' column to indicate forecast day
df['Day'] = range(1, len(df) + 1)

# Initialize the figure
fig = go.Figure()

# Set initial offset
offset = -0.15

# Add bars for each city
for city in df.columns[:-1]:  # Exclude the 'Day' column
    fig.add_trace(go.Bar(
        x=df['Day'] + offset,  # Position on the x-axis
        y=df[city],            # Data for each city
        name=city,             # Legend label
        width=0.1,             # Bar width
        # Make each bar semi-transparent for overlay effect
        marker=dict(opacity=0.6)
    ))
    offset += 0.1  # Increment offset for next city

# Styling the layout
fig.update_layout(
    # Main title and fonts
    title={
        'text': '5-Day Temperature Forecast for Multiple Cities',
        'font': {'size': 24}
    },
    # X-axis settings
    xaxis={
        'title': 'Day',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14}
    },
    # Y-axis settings
    yaxis={
        'title': 'Temperature (°C)',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14}
    },
    # Legend settings
    legend={
        'font': {'size': 16}
    },
    # Background color
    plot_bgcolor='rgba(255,255,255,0.9)',
    # Overlay bar mode
    barmode='overlay'
)

# Show the plot
fig.show()
