import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import plotly.graph_objects as go

load_dotenv()

def fetch_movie_data(page_number, file_name="top_mivies.json"):
    api_key = os.getenv("TMDb_API_KEY")
    if not api_key:
        print("API key not found.")
        return None

    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={page_number}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['results']

        # Saving data to file
        with open(file_name, "w") as f:
            json.dump(data, f)

        return data
    else:
        print(f"Failed to get data: {response.status_code}")
        return None


def display_images(poster_paths):
    urls = ["https://image.tmdb.org/t/p/w500" + poster_path for poster_path in poster_paths]
    plt.figure(figsize=(18,5), tight_layout=True)
    for i, url in enumerate(urls):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        plt.subplot(1, len(urls), i+1)
        plt.imshow(img)
        plt.axis('off')
    plt.subplots_adjust(left=0.5, right=0.9, top=0.9, bottom=0.1)
    plt.show()


def plot_movie_data(movies, num):
    names = [movie['title'] for movie in movies]
    popularity = [movie['popularity'] for movie in movies]
    vote_average = [movie['vote_average'] for movie in movies]
    release_dates = [movie['release_date'] for movie in movies]

    fig = go.Figure()

    fig.add_trace(go.Bar(x=names, y=popularity, name='Popularity', marker=dict(color='blue', line=dict(color='yellow', width=3.5), pattern_shape="x")))

    fig.add_trace(go.Scatter(x=names, y=vote_average, mode='lines+markers', name='Vote Average', yaxis='y2', line=dict(color='red', width=6), marker=dict(size=18, color='darkred')))

    annotations = [dict(x=xi, y=0, yref="y2", xref="x", text=str(d), showarrow=True, font=dict(family="Arial, sans-serif", size=18, color="yellow")) for xi, d in zip(names, release_dates)]

    fig.update_layout(
        title=dict(text=f'🎦 Top {num} Movies [& release date]'),
        xaxis=dict(title='🎥 Movies'),
        yaxis=dict(title='📊 Popularity'),
        yaxis2=dict(title='📈 Vote Average', overlaying='y', side='right'),
        font=dict(family="Arial, sans-serif", size=20, color="darkblue"),
        plot_bgcolor='deepskyblue',
        width=1800,
        height=900,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        annotations=annotations
    )

    fig.show()


if __name__ == "__main__":
    page_number = 1
    movies_number = 8
    movies = fetch_movie_data(page_number)
    if movies:
        top_movies = sorted(movies, key=lambda x: x['popularity'], reverse=True)[:movies_number]
        poster_paths = [movie['poster_path'] for movie in top_movies]
        display_images(poster_paths)
        plot_movie_data(top_movies, movies_number)
