def fetch_current_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)['main']['temp']  # Получаем температуру в градусах Цельсия
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

cities = ['Alta', 'Ufa', 'Anadyr', 'Tokyo', 'Cape Town', 'Wellington', 'Toronto', 'Rio de Janeiro']

weather_data = {}
for city in cities:
    temp = fetch_current_weather(city, api_key)
    if temp is not None:
        weather_data[city] = temp  # Сохраняем текущую температуру

df = pd.DataFrame([weather_data], index=['Temperature'])
df.to_csv('current_weather_data.csv', index=True)
df.head()
