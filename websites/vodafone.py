import requests
import json

movie = []
tv_show = []
url = "https://api.vodafoneplay.in/content/v7/search/?fields=generalInfo,images,relatedCast,\
        publishingHouse,contents,relatedMedia,reviews/user,globalServiceId&&level=&query={}&\
        startIndex=1&count=10&orderBy=releaseDate&orderMode=1&publishingHouseId=1,5,10,43,51,52,\
        53,55,56,57,58,59,61,63,65,66,67,69,71,80,81,82,83,85,86,100&type=movie%2Cvodchannel%2Ctvshow%2Ctvseries%2Clive"
link = "https://www.vodafoneplay.in/{}/detail/{}/{}"


def find(name):
    global movie, tv_show, url, link
    r = requests.get(url.format(name))
    y = json.loads(r.text)
    for i in y['results']:
        if i['generalInfo']['type'] == "movie":
            movie.append((i['generalInfo']['title'], link.format("movies", i["_id"], i['generalInfo']['title']), True))
        else:
            tv_show.append((i['generalInfo']['title'], link.format("tvshows", i["_id"], i['generalInfo']['title']), False))


def voda_search(name, type=None):
    print("vodafone")
    find(name)
    global movie, tv_show
    if type == "movie":
        return movie
    elif type == "show":
        return tv_show
    else:
        if movie and tv_show:
            return movie + tv_show
        elif movie:
            return movie
        elif tv_show:
            return tv_show
        else:
            return None


if __name__ == "__main__":
    print(voda_search("dabang"))