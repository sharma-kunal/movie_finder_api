import requests

endpoint = "https://search.airtel.tv/app/v3/search/atv/query?appId=WEB&bn=15&count=30&dt=BROWSER&ln=hi&offSet=0&os=WEBOS&q={}"
link = "https://www.airtelxstream.in/{}/{}"


def airtel_search(name, type=None):
    print("airtel")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        try:
            data = response.json()['categories']
            movie_data, series_data = [], []
            for d in data:
                if d['type'] == "MOVIE":
                    movie_data = d['contentResponseList']
                elif d['type'] == "TVSHOW":
                    series_data = d['contentResponseList']
            if type == "movie":
                return find_movie(movie_data)
            elif type == "show":
                return find_show(series_data)
            else:
                movies = find_movie(movie_data)
                series = find_show(series_data)
                if movies and series:
                    return movies + series
                elif movies:
                    return movies
                elif series:
                    return series
                else:
                    return None
        except Exception as e:
            print(e)
            return None
    else:
        return None


def find_movie(data):
    movies = []
    for d in data:
        movies.append((d['title'], link.format("movies", d['id']), True))
    return movies


def find_show(data):
    series = []
    for d in data:
        series.append((d['title'], link.format("tv-shows", d['id']), False))
    return series


if __name__ == "__main__":
    for d in airtel_search("avengers"):
        print(d)