import requests

endpoint = "https://api.cloud.altbalaji.com/media/videos?query={}&tags[]=&limit=50&offset=0&domain=IN"
url = "https://altbalaji.com/{}/{}"
name_link = "https://api.cloud.altbalaji.com/media/series/{}?domain=IN"


def alt_balaji_search(name, type=None):
    print("alt balaji")
    counter = 0
    response = None
    while counter < 3:
        try:
            response = requests.get(endpoint.format(name))
            break
        except Exception:
            counter += 1
    if response.status_code == 200:
        data = response.json()['media']
        return find_movie_and_show(data, type)
    return None


def find_movie_and_show(data, type):
    movies, shows = [], []
    names = []
    ids = []
    for i, d in enumerate(data):
        counter = 0
        while counter < 2:
            try:
                if d['tags'][0] == "type-movie":
                    movies.append((d['titles']['default'], url.format("media", d['id']), True))
                    break
                elif d['tags'][0] == "type-episode":
                    id_ = d['_links']['series']['href'].split("/")[-1]
                    name_response = requests.get(name_link.format(id_))
                    if name_response.status_code == 200:
                        name = name_response.json()['titles']['default']
                        if name not in names and id_ not in ids:
                            shows.append((name, url.format("show", id_), False))
                            names.append(name)
                            ids.append(id_)
                        break
                    else:
                        counter += 1
                else:
                    break
            except Exception:
                counter += 1
    if type == "movie":
        return movies or None
    elif type == "series":
        return shows or None
    else:
        if movies and shows:
            return movies + shows
        elif movies:
            return movies
        elif shows:
            return shows
        else:
            return None


if __name__ == "__main__":
    for i in alt_balaji_search("avengers"):
        print(i)