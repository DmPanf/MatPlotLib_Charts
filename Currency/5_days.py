import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

# Загрузим переменные окружения
load_dotenv()

# Получим API ключ из переменных окружения
api_key = os.getenv('OPEN_WEATHER_MAP_API_KEY')

# Определим города, для которых хотим получить прогноз
cities = ['Alta', 'Ufa', 'Anadyr', 'Tokyo', 'Cape Town', 'Wellington', 'Toronto', 'Rio de Janeiro']

# Функция для получения 5-дневного прогноза погоды
def fetch_5_day_forecast(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        # Получим только дневные прогнозы (по одному на день)
        daily_forecast = [forecast for forecast in json.loads(response.text)['list'] if '12:00:00' in forecast['dt_txt']]
        return [entry['main']['temp'] for entry in daily_forecast]  # Вернем список температур в градусах Цельсия
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

# Инициализируем пустой словарь для данных о погоде
weather_data = {}

# Переберем все города и получим для них 5-дневный прогноз
for city in cities:
    forecast_data = fetch_5_day_forecast(city, api_key)
    if forecast_data:
        weather_data[city] = forecast_data

# Преобразуем данные в DataFrame и сохраняем их в CSV файл
df = pd.DataFrame(weather_data)
df.to_csv('5_day_weather_data.csv', index=False)

# Показываем первые 5 строк DataFrame
df.head()
