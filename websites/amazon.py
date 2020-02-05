import requests
import traceback
import json

link = "https://www.jiocinema.com/watch/{}/{}/0/0/{}/0/0"


def searchApi(query):
    endpoint = "http://prod.media.jio.com/apis/common/v3.1/search/search"
    data = {
        "q": query
    }
    try:
        response = requests.post(endpoint, data=data)
        if response.status_code == 200:
            data = response.json()
            movie_data = ""
            series_data = ""
            for d in data['data']['items']:
                if d['name'] == "Movies":
                    movie_data = d
                elif d['name'] == "TV Shows":
                    series_data = d
    except Exception:
        print(traceback.format_exc())


def find_movie(data):
    movies = []
    for movie in data['items']:
        movies.append((movie['name'], link.format("movies", movie['name'], movie['id']), True))
    return movies

searchApi("avengers")