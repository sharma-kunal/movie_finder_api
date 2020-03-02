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
<<<<<<< HEAD
    def get(self, response):
=======
    def get(self, request):
>>>>>>> 1752aec8129ff9d787b05960cab4b0227ea6361f
        movie_name = self.request.query_params.get('name', None)
        # flag = self.request.query_params.get('flag', None)
        type_ = self.request.query_params.get('type', None)
        if movie_name:
            options = Options()
            options.add_argument("--headless")
            browser = webdriver.Chrome(chrome_options=options)
            # print(movie_name)
            data = []
            hotstar = hotstar_search(movie_name, browser, type_)
            airtel = airtel_search(movie_name, type_)
            eros_now = eros_search(movie_name, type_)
            jio = jio_search(movie_name, type_)
            idea = idea_search(movie_name, browser)
            vodafone = voda_search(movie_name, type_)
            zee5 = zee5_search(movie_name, type_)
            mx_player = mx_player_search(movie_name, type_)
            alt_balaji = alt_balaji_search(movie_name, type_)
            if hotstar:
                data = [Data(name=mn, provider="hotstar", link=link, movie=typ) for mn, link, typ in hotstar]
            if airtel:
                data += [Data(name=mn, provider="airtel", link=link, movie=typ) for mn, link, typ in airtel]
            if eros_now:
                data += [Data(name=mn, provider="eros_now", link=link, movie=typ) for mn, link, typ in eros_now]
            if jio:
                data += [Data(name=mn, provider="jio_cinema", link=link, movie=typ) for mn, link, typ in jio]
            if idea:
                data += [Data(name=mn, provider="idea", link=link, movie=typ) for mn, link, typ in idea]
            if vodafone:
                data += [Data(name=mn, provider="vodafone", link=link, movie=typ) for mn, link, typ in vodafone]
            if zee5:
                data += [Data(name=mn, provider="zee5", link=link, movie=typ) for mn, link, typ in zee5]
            if mx_player:
                data += [Data(name=mn, provider="mx_player", link=link, movie=typ) for mn, link, typ in mx_player]
            if alt_balaji:
                data += [Data(name=mn, provider="alt_balaji", link=link, movie=typ) for mn, link, typ in alt_balaji]
            serializer = DataSerializer(data, many=True)
            return Response(serializer.data)
