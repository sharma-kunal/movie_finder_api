import requests, json


endpoint = "https://pwaproxy.erosnow.com/api/v2/search?q={}&start=0&rows=10&optimized=true&country=IN"
url = "https://erosnow.com/{}/watch/{}/{}"


def eros_search(name, type=None):
    print("eros now")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = json.loads(response.text)
        movies_data, series_data, originals = "", "", ""
        if data.get("movies", None):
            movies_data = data['movies']['rows']
        if data.get("tvshow", None):
            series_data = data['tvshow']['rows']
        if data.get("originals", None):
            originals = data['originals']['rows']
        if type == "movie":
            return find_movie(movies_data)
        elif type == "tv_show":
            return find_series(series_data)
        else:
            movies = find_movie(movies_data)
            series = find_series(series_data)
            if movies and series:
                return movies +series
            elif movies:
                return movies
            elif series:
                return series
            else:
                return None
    else:
        return None


def find_movie(data):
    movies = []
    try:
        for movie in data:
            movies.append((movie['title'], url.format("movie", movie['asset_id'], movie['title']), True))
        return movies
    except KeyError:
        return None


def find_series(data):
    series = []
    try:
        for show in data:
            series.append((show['title'], url.format("tv", show['asset_id'], show['title']), False))
        return series
    except KeyError:
        return None


if __name__ == "__main__":
    print(eros_search("avengers"))