import pandas as pd
import plotly.express as px

# Загрузим данные из CSV-файла в DataFrame
df = pd.read_csv('5_day_weather_data.csv')

# Модифицируем DataFrame так, чтобы он был подходящим для Plotly
df_melted = pd.melt(df, var_name='City', value_name='Temperature')
df_melted['Day'] = df_melted.groupby('City').cumcount() + 1  # Добавляем дни

# Создаем график
fig = px.line(df_melted, x='Day', y='Temperature', color='City',
              title='5-Day Temperature Forecast for Multiple Cities',
              labels={'Temperature': 'Temperature (°C)', 'Day': 'Forecast Day'})

# Отображаем график
fig.show()
