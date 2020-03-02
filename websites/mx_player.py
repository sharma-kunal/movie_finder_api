import requests

endpoint = "https://api.mxplay.com/v1/web/search/result/list?q={}&query={}&queryId=\
            NtJkcA4p-vyHQmohlA4sZ&search=true&sectionId={}&type={}&userid=e7727c7d-cf9c-4e27-8dd9-b73a\
            7592ca62&platform=com.mxplay.desktop&content-languages=hi,en"
url = "https://www.mxplayer.in"


def mx_player_search(name, type=None):
    print("mx player")
    response = None
    counter = 0
    if type == "movie":
        while counter < 3:
            try:
                response = requests.get(endpoint.format(name, name, "movie", "movie"))
                break
            except Exception:
                counter += 1
        try:
            if response and response.status_code == 200:
                data = response.json()['items']
                return find_movie(data)
            else:
                return None
        except KeyError:
            return None
    elif type == "show":
        while counter < 3:
            try:
                response = requests.get(endpoint.format(name, name, "shows", "shows"))
                break
            except Exception:
                counter += 1
        try:
            if response and response.status_code == 200:
                data = response.json()['items']
                return find_series(data)
        except KeyError:
            return None
    else:
        movies, series = [], []
        movie_response, series_response = None, None
        while counter < 3:
            try:
                movie_response = requests.get(endpoint.format(name, name, "movie", "movie"))
                break
            except Exception:
                counter += 1
        try:
            if movie_response and movie_response.status_code == 200:
                movie_data = movie_response.json()['items']
                movies = find_movie(movie_data)
            else:
                return None
        except KeyError:
            return None
        while counter < 3:
            try:
                series_response = requests.get(endpoint.format(name, name, "shows", "shows"))
                break
            except Exception:
                counter += 1
        try:
            if series_response and series_response.status_code == 200:
                series_data = series_response.json()['items']
                series = find_series(series_data)
            else:
                return None
        except KeyError:
            return None
        if movies and series:
            return movies + series
        elif movies:
            return movies
        elif series:
            return series
        else:
            return None


def find_movie(data):
    movies = []
    try:
        for movie in data:
            movies.append((movie['title'], url + movie['shareUrl'], True))
        return movies
    except KeyError:
        return None


def find_series(data):
    series = []
    try:
        for show in data:
            series.append((show['title'], url + show['shareUrl'], False))
        return series
    except KeyError:
        return None


if __name__ == "__main__":
    print(mx_player_search("avengers"))