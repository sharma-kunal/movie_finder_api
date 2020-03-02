import requests
import json

url = "https://gwapi.zee5.com/content/getContent/search?q={}&start=0&limit=24&asset_type=0,6,1&country=IN&\
        languages=en,hi,pa&translation=en&version=3&page=1"
link = "https://www.zee5.com/{}/details/{}/{}"


def find_movie(data):
    movie = []
    try:
        for movies in data['movies']:
            movie.append((movies['title'], link.format("movies", movies['title'], movies['id']), True))
        return movie
    except KeyError:
        return None


def find_show(data):
    try:
        tv_show = []
        for show in data['tvshows']:
            tv_show.append((show['title'], link.format("tvshows", show['title'], show['id']), False))
        return tv_show
    except KeyError:
        return None


def zee5_search(name, type=None):
    print("zee 5")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(url.format(name))
            break
        except Exception:
            counter += 1
    if response and response.status_code == 200:
        data = response.json()
        movie, show = [], []
        if type == "movie":
            movie = find_movie(data)
        elif type == "show":
            show = find_show(data)
        else:
            movie = find_movie(data)
            show = find_show(data)
        if movie and show:
            return movie + show
        elif movie:
            return movie
        elif show:
            return show
        else:
            return None


if __name__ == "__main__":
    print(zee5_search("bal"))
