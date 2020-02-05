import requests

link = "https://www.jiocinema.com/watch/{}/{}/0/0/{}/0/0"
endpoint = "http://prod.media.jio.com/apis/common/v3.1/search/search"


def jio_search(name, type=None):
    print("jio")
    data = {
        "q": name
    }
    try:
        counter = 0
        response = None
        while counter < 3:
            try:
                response = requests.post(endpoint, data=data)
                break
            except Exception:
                counter += 1
        if response and response.status_code == 200:
            data = response.json()
            movie_data = ""
            series_data = ""
            movies, tv_series = [], []
            try:
                for d in data['data']['items']:
                    if d['name'] == "Movies":
                        movie_data = d
                    elif d['name'] == "TV Shows":
                        series_data = d
            except KeyError:
                pass
            if type == "movie" and movie_data:
                movies = find_movie(movie_data)
            elif type == "tv_show" and series_data:
                tv_series = find_series(series_data)
            else:
                movies = find_movie(movie_data)
                tv_series = find_series(series_data)
            if movies and tv_series:
                return movies + tv_series
            elif movies:
                return movies
            elif tv_series:
                return tv_series
            else:
                return None
    except Exception:
        return None


def find_movie(data):
    try:
        movies = []
        for movie in data['items']:
            movies.append((movie['name'], link.format("movies", movie['name'], movie['id']), True))
        return movies
    except KeyError:
        return None


def find_series(data):
    try:
        series = []
        for show in data['items']:
            series.append((show['name'], link.format("tv", show['name'], show['id']), False))
        return series
    except KeyError:
        return None


if __name__ == "__main__":
    print(jio_search("avengers"))