import requests, json
from requests.auth import HTTPBasicAuth

endpoint = "https://api.hotstar.com/s/v1/scout?q={}&perPage=50"


def hotstar_search(name, type=None):
    print(endpoint.format(name))
    response = requests.post(endpoint.format(name), auth=HTTPBasicAuth('user', 'pass'))
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("error")


hotstar_search("avengers")