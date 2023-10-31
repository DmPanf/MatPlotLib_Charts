import requests
from IPython.core.display import display, HTML

# api_key = "541a1398160b1ed6903fbf4716a83389"

def fetch_movie_data(page_number, api_key='541a1398160b1ed6903fbf4716a83389'):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={page_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Failed to get data: {response.status_code}")
        return None

def display_movie_info(movie):
    title = movie['title']
    overview = movie['overview']
    popularity = movie['popularity']
    release_date = movie['release_date']
    vote_average = movie['vote_average']
    vote_count = movie['vote_count']
    poster_path = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

    html_str = f"""
    <div style="border:2px solid black; margin:20px; padding:20px;">
        <h2>{title}</h2>
        <img src="{poster_path}" alt="Poster" style="float:left; margin-right:20px; width:200px;">
        <p><b>Overview:</b> {overview}</p>
        <p><b>Popularity:</b> {popularity}</p>
        <p><b>Release Date:</b> {release_date}</p>
        <p><b>Vote Average:</b> {vote_average}</p>
        <p><b>Vote Count:</b> {vote_count}</p>
    </div>
    """
    display(HTML(html_str))

# Запрашиваем номер страницы от пользователя
page_number = input("Enter the page number: ")

# Получаем данные с этой страницы
movies = fetch_movie_data(page_number)

# Выводим информацию о каждом фильме на этой странице
if movies:
    for movie in movies:
        display_movie_info(movie)
