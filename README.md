# Movie Finding API

This is a Django REST-API for finding movies online on around 9 platforms (will keep on adding more). It searches for a given movie on different streaming platforms. Some are mentioned below:

* Airtel Xstream
* Eros Now
* MX Player
* Jio Cinema
* Vodafone Play
* Zee5
* Alt Balaji

## Installation

You need to install Django and Django Rest Framework and selenium (for scraping Hotstar). Just run the commands

```
pip install Django==3.0.2
pip install djangorestframework==3.11.0
pip install selenium==3.141.0
```

and you are good to go.

## Running

1. First you need to start the django api using the command 

```
python manage.py runserver
```

---
**NOTE**

Please make sure that you are in the directory where manage.py is present

---

2. Now just for testing purposes I have provided a file `client.py`. You can run this file to check the result fetched by API.
You can run the file and type any movie name you want to search and it will search on all platforms for the given movie and provide you all the results fetched

## Further Improvements

Currently the project is in development phase as there are many improvements that need to be done and many more functionalities that need to be added to the project. Some are

* I can't get the API for Amazon Prime Videos, Netflix and other providers. So whenever I get the access to API I will add them to the project
* I was using selenium to find results on Hotstar, because I can't find a way to access their API.
* An app interface would be nice to show the results more delightful for the user.

If you have any doubts regarding the project, feel free to message me.
If you want to contribute to the project, feel free to do so.

Happy Coding :)
