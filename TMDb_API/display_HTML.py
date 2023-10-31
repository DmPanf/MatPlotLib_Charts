from IPython.core.display import display, HTML

def display_movie_info(movie):
    # Получение данных из JSON
    title = movie['title']
    overview = movie['overview']
    popularity = movie['popularity']
    release_date = movie['release_date']
    vote_average = movie['vote_average']
    vote_count = movie['vote_count']
    poster_path = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

    # Создание HTML-строки
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

    # Вывод HTML
    display(HTML(html_str))

# Пример использования с вашим JSON-ответом
movie = {
    'adult': False,
    'backdrop_path': '/t5zCBSB5xMDKcDqe91qahCOUYVV.jpg',
    'genre_ids': [27],
    'id': 507089,
    'original_language': 'en',
    'original_title': "Five Nights at Freddy's",
    'overview': "Recently fired and desperate for work, a troubled young man named Mike agrees to take a position as a night security guard at an abandoned theme restaurant: Freddy Fazbear's Pizzeria. But he soon discovers that nothing at Freddy's is what it seems.",
    'popularity': 5089.151,
    'poster_path': '/A4j8S6moJS2zNtRR8oWF08gRnL5.jpg',
    'release_date': '2023-10-25',
    'title': "Five Nights at Freddy's",
    'video': False,
    'vote_average': 8.442,
    'vote_count': 840
}

display_movie_info(movie)
