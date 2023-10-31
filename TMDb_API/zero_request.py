import requests
import json

# URL для запроса популярных фильмов
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page=1"

# Выполнение GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Расшифровка JSON-ответа
    data = json.loads(response.text)

    # Печать информации о первом популярном фильме
    print(data['results'][0])
else:
    print(f"Failed to get data: {response.status_code}")
