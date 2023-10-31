import requests
import json
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPEN_WEATHER_MAP_API_KEY')

cities = ['Alta', 'Ufa', 'Anadyr', 'Tokyo', 'Cape Town', 'Wellington', 'Toronto', 'Rio de Janeiro']

def fetch_weather_data(city, start_date, end_date, api_key):
    lat = city['lat']
    lon = city['lon']

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())


    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={start_timestamp}&appid={api_key}"
    print('\n', url)

    params = {'api_key': api_key}
    response = requests.get(url, params=params)


    if response.status_code == 200:
        weather_data = json.loads(response.text)
        avg_temp = weather_data['current']['temp']  # Temperature is in Kelvin
        avg_temp = avg_temp - 273.15  # Convert to Celsius
        return avg_temp
    else:
        print(f"Failed to get data: {response.status_code}")
        return None




def save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

city_coordinates = [
    {'name': 'Alta', 'lat': 69.9689, 'lon': 23.2717},
    {'name': 'Ufa', 'lat': 54.7355, 'lon': 55.9587},
    {'name': 'Anadyr', 'lat': 64.7337, 'lon': 177.4966},
    {'name': 'Tokyo', 'lat': 35.6895, 'lon': 139.6917},
    {'name': 'Cape Town', 'lat': -33.9249, 'lon': 18.4241},
    {'name': 'Wellington', 'lat': -41.2925, 'lon': 174.7730},
    {'name': 'Toronto', 'lat': 43.651070, 'lon': -79.347015},
    {'name': 'Rio de Janeiro', 'lat': -22.9083, 'lon': -43.1964},
]


start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 1)

weather_data = {}
for city in city_coordinates:
    weather_data[city['name']] = []

    current_date = start_date
    while current_date <= end_date:
        temp = fetch_weather_data(city, current_date, current_date, api_key)
        if temp is not None:
            weather_data[city['name']].append(temp)
        current_date += timedelta(days=1)

save_to_file(weather_data, 'weather_data.json')

# Преобразуем данные в DataFrame для вывода
df = pd.DataFrame(weather_data)
print(df)
