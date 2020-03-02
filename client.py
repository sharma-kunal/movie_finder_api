import requests, json, time
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = '<YOUR API KEY>'

type = input("What do you want to search for? Movie or Show: (m/s) (leave blank for None): ")
if type.lower() == "m":
    type = "movie"
elif type.lower() == "s":
    type = "show"
else:
    type = None
name = input("Enter name: ")
movie = Movie()
search = movie.search(name)

di = {}
for i, res in enumerate(search):
    di[i+1] = res
    print(f"{i+1}\t{res}")
if len(di.keys()) == 0:
    raise Exception("No movies found..")
num = input("\nSelect the movie number: ")
try:
    name = di[int(num)]
except KeyError:
    raise Exception("Please select valid number from above.")

url = f'http://localhost:8000/api/data/?name={name}&type={type}'
curr = time.time()
response = requests.get(url)
result = response.text
result = json.loads(result)
hotstar_movies, hotstar_series = [], []
airtel_movies, airtel_series = [], []
eros_movies, eros_series = [], []
idea_movies, idea_series = [], []
voda_movies, voda_series = [], []
zee5_movies, zee5_series = [], []
jio_movies, jio_series = [], []
mx_movies, mx_series = [], []
alt_balaji_movies, alt_balaji_series = [], []
if not result:
    print("No result found")
for res in result:
    if res['provider'] is None:
        print("No result found")
        break
    if res['movie']:
        if res['provider'] == "hotstar":
            hotstar_movies.append(res)
        elif res['provider'] == "airtel":
            airtel_movies.append(res)
        elif res['provider'] == "eros_now":
            eros_movies.append(res)
        elif res['provider'] == "idea":
            idea_movies.append(res)
        elif res['provider'] == "vodafone":
            voda_movies.append(res)
        elif res['provider'] == "zee5":
            zee5_movies.append(res)
        elif res['provider'] == "jio_cinema":
            jio_movies.append(res)
        elif res['provider'] == "mx_player":
            mx_movies.append(res)
        elif res['provider'] == "alt_balaji":
            alt_balaji_movies.append(res)
    elif not res['movie']:
        if res['provider'] == "hotstar":
            hotstar_series.append(res)
        elif res['provider'] == "airtel":
            airtel_series.append(res)
        elif res['provider'] == "eros_now":
            eros_series.append(res)
        elif res['provider'] == "idea":
            idea_series.append(res)
        elif res['provider'] == "vodafone":
            voda_series.append(res)
        elif res['provider'] == "zee5":
            zee5_series.append(res)
        elif res['provider'] == "jio_cinema":
            jio_series.append(res)
        elif res['provider'] == "mx_player":
            mx_series.append(res)
        elif res['provider'] == "alt_balaji":
            alt_balaji_series.append(res)
if hotstar_movies or hotstar_series:
    print("\nHotstar\n")
    if hotstar_movies:
        print("Movies\n")
        for i, val in enumerate(hotstar_movies):
            print(val['name'] + "\t" + val['link'])
    if hotstar_series:
        print("\nTV Shows\n")

        for i, val in enumerate(hotstar_series):
            print(val['name'] + "\t" + val['link'])

if airtel_movies or airtel_series:
    print("\nAirtel\n")
    if airtel_movies:
        print("Movies\n")
        for i, val in enumerate(airtel_movies):
            print(val['name'] + "\t" + val['link'])
    if airtel_series:
        print("\nTV Shows\n")
        for i, val in enumerate(airtel_series):
            print(val['name'] + "\t" + val['link'])

if eros_movies or eros_series:
    print("\nEros Now\n")
    if eros_movies:
        print("Movies\n")
        for i, val in enumerate(eros_movies):
            print(val['name'] + "\t" + val['link'])
    if eros_series:
        print("\nTV Shows\n")
        for i, val in enumerate(eros_series):
            print(val['name'] + "\t" + val['link'])

if idea_movies or idea_series:
    print("\nIdea Movies & TV\n")
    if idea_movies:
        print("Movies\n")
        for i, val in enumerate(idea_movies):
            print(val['name'] + "\t" + val['link'])
    if idea_series:
        print("\nTV Shows\n")
        for i, val in enumerate(idea_series):
            print(val['name'] + "\t" + val['link'])

if voda_movies or voda_series:
    print("\nVodafone Play\n")
    if voda_movies:
        print("Movies\n")
        for i, val in enumerate(voda_movies):
            print(val['name'] + "\t" + val['link'])
    if voda_series:
        print("\nTV Shows\n")
        for i, val in enumerate(voda_series):
            print(val['name'] + "\t" + val['link'])

if zee5_movies or zee5_series:
    print("\nZee5\n")
    if zee5_movies:
        print("Movies\n")
        for i, val in enumerate(zee5_movies):
            print(val['name'] + "\t" + val['link'])
    if zee5_series:
        print("\nTV Shows\n")
        for i, val in enumerate(zee5_series):
            print(val['name'] + "\t" + val['link'])

if jio_movies or jio_series:
    print("\nJio Cinema\n")
    if jio_movies:
        print("Movies\n")
        for i, val in enumerate(jio_movies):
            print(val['name'] + "\t" + val['link'])
    if jio_series:
        print("\nTV Shows\n")
        for i, val in enumerate(jio_series):
            print(val['name'] + "\t" + val['link'])

if mx_movies or mx_series:
    print("\nMX Player\n")
    if mx_movies:
        print("Movies\n")
        for i, val in enumerate(mx_movies):
            print(val['name'] + "\t" + val['link'])
    if mx_series:
        print("\nTV Shows\n")
        for i, val in enumerate(mx_series):
            print(val['name'] + "\t" + val['link'])

if alt_balaji_movies or alt_balaji_series:
    print("\nAlt Balaji\n")
    if alt_balaji_movies:
        print("Movies\n")
        for i, val in enumerate(alt_balaji_movies):
            print(val['name'] + "\t" + val['link'])
    if alt_balaji_series:
        print("\nTV Shows\n")
        for i, val in enumerate(alt_balaji_series):
            print(val['name'] + "\t" + val['link'])

print(time.time()-curr)
