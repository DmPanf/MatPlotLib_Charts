import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_WEATHER_MAP_API_KEY')

# cities = ['Alta', 'Ufa', 'Anadyr', 'Tokyo', 'Cape Town', 'Wellington', 'Toronto', 'Rio de Janeiro']

cities = [
    {'name': 'Alta', 'lat': 69.9689, 'lon': 23.2717},
    {'name': 'Ufa', 'lat': 54.7355, 'lon': 55.9587},
    {'name': 'Anadyr', 'lat': 64.7337, 'lon': 177.4966},
    {'name': 'Tokyo', 'lat': 35.6895, 'lon': 139.6917},
    {'name': 'Cape Town', 'lat': -33.9249, 'lon': 18.4241},
    {'name': 'Wellington', 'lat': -41.2925, 'lon': 174.7730},
    {'name': 'Toronto', 'lat': 43.651070, 'lon': -79.347015},
    {'name': 'Rio de Janeiro', 'lat': -22.9083, 'lon': -43.1964},
]

def fetch_10_day_forecast(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)['daily']
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

weather_data = {}
for city in cities:
    forecast_data = fetch_10_day_forecast(city['lat'], city['lon'], api_key)
    if forecast_data:
        weather_data[city['name']] = [day['temp']['day'] - 273.15 for day in forecast_data]  # Конвертируем из Кельвинов в Цельсии

df = pd.DataFrame(weather_data)
df.to_csv('weather_data.csv', index=False)
df.head(10)
