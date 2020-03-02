from rest_framework.views import APIView
from rest_framework.response import Response
from selenium import webdriver
from rest_framework import status
from .serializers import *
from websites.hotstar_selenium import hotstar_search
from websites.airtel import airtel_search
from websites.eros_now import eros_search
from websites.jio import jio_search
from websites.vodafone import voda_search
from websites.idea import idea_search
from websites.zee5 import zee5_search
from websites.mx_player import mx_player_search
from websites.alt_balaji import alt_balaji_search
from .models import Data
from selenium.webdriver.chrome.options import Options


class DataList(APIView):
    def get(self, response):
        movie_name = self.request.query_params.get('name', None)
        type_ = self.request.query_params.get('type', None)
        data = find_in_database(movie_name, [])
        if movie_name and not data:
            options = Options()
            options.add_argument("--headless")
            browser = webdriver.Chrome(chrome_options=options)
            # print(movie_name)
            # hotstar = hotstar_search(movie_name, browser, type_)
            airtel = airtel_search(movie_name, type_)
            eros_now = eros_search(movie_name, type_)
            jio = jio_search(movie_name, type_)
            idea = idea_search(movie_name, browser)
            vodafone = voda_search(movie_name, type_)
            zee5 = zee5_search(movie_name, type_)
            mx_player = mx_player_search(movie_name, type_)
            alt_balaji = alt_balaji_search(movie_name, type_)
            # if hotstar:
            #     for mn, link, typ in hotstar:
            #         temp = Data(name=mn, provider="hotstar", link=link, movie=typ)
            #         temp.save()
            #         data.append(temp)
            if airtel:
                for mn, link, typ in airtel:
                    temp = Data(name=mn, provider="airtel", link=link, movie=typ)
                    temp.save()
            if eros_now:
                for mn, link, typ in eros_now:
                    temp = Data(name=mn, provider="eros_now", link=link, movie=typ)
                    temp.save()
            if jio:
                for mn, link, typ in jio:
                    temp = Data(name=mn, provider="jio_cinema", link=link, movie=typ)
                    temp.save()
            if idea:
                for mn, link, typ in idea:
                    temp = Data(name=mn, provider="idea", link=link, movie=typ)
                    temp.save()
            if vodafone:
                for mn, link, typ in vodafone:
                    temp = Data(name=mn, provider="vodafone", link=link, movie=typ)
                    temp.save()
            if zee5:
                for mn, link, typ in zee5:
                    temp = Data(name=mn, provider="zee5", link=link, movie=typ)
                    temp.save()
            if mx_player:
                for mn, link, typ in mx_player:
                    temp = Data(name=mn, provider="mx_player", link=link, movie=typ)
                    temp.save()
            if alt_balaji:
                for mn, link, typ in alt_balaji:
                    temp = Data(name=mn, provider="alt_balaji", link=link, movie=typ)
                    temp.save()
            data = find_in_database(movie_name, [])
            if not data:
                temp = Data(name=movie_name, provider=None, link=None, movie=False)
                temp.save()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)


def find_in_database(movie_name, data):
    database = Data.objects.all()
    for d in database:
        if d.name == movie_name:
            data.append(Data(name=d.name, provider=d.provider, link=d.link, movie=d.movie))
    return data