import pandas as pd
import plotly.graph_objects as go

# Предположим, что df содержит ваш DataFrame с данными о погоде
df = pd.read_csv('5_day_weather_data.csv')

# Добавим столбец с днями прогноза
df['Day'] = range(1, len(df) + 1)

# Инициализируем фигуру
fig = go.Figure()

# Добавляем данные для каждого города
offset = -0.15  # начальное смещение
for city in df.columns[:-1]:  # исключаем столбец 'Day'
    fig.add_trace(go.Bar(
        x=df['Day'] + offset,
        y=df[city],
        name=city,
        width=0.1  # ширина столбца
    ))
    offset += 0.1  # увеличиваем смещение для следующего города

# Настраиваем layout
fig.update_layout(
    title='5-Day Temperature Forecast for Multiple Cities',
    xaxis=dict(title='Day'),
    yaxis=dict(title='Temperature (°C)'),
    barmode='overlay'
)

# Показываем график
fig.show()
