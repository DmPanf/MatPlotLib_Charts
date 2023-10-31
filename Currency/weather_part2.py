import pandas as pd
import plotly.graph_objects as go

# Читаем данные из файла
df = pd.read_csv('weather_data.csv')

fig = go.Figure()

for city in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[city], mode='lines+markers', name=city))

fig.update_layout(
    title="10-day Weather Forecast",
    xaxis_title="Day",
    yaxis_title="Temperature (°C)"
)

fig.show()
