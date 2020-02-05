from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from bs4 import BeautifulSoup
import time


def hotstar_search(name, browser, typ=None):

    # No need to encode movie_name (it works fine without encoding)
    print("hotstar")
    curr_time = time.time()
    # encoded_movie_name = ur.quote_plus(movie_name)
    # encoded_movie_name = encoded_movie_name.replace("+", " ")
    # print(encoded_movie_name)
    browser.get(f'https://www.hotstar.com/in/search?q={name}')

    # Movies
    if typ == "movie":
        return find_movie(browser)

    # TV Show
    elif typ == "tv_show":
        return find_show(browser)

    # typ = None
    else:
        movie = find_movie(browser)
        show = find_show(browser)
        print("Hotstar time: " + str(time.time()-curr_time))
        if movie and show:
            return movie + show
        elif movie:
            return movie
        elif show:
            return show
        else:
            return None


def find_movie(browser):
    # Finding Movie Links
    try:
        src = WebDriverWait(browser, 2).until(
            ec.presence_of_all_elements_located((By.XPATH, "//article[@class='ripple movie-card normal']"))
        )
        links = [s.find_element_by_tag_name('a').get_attribute('href') for s in src]
    except TimeoutException:
        return None
    names = []
    for divs in src:
        div = divs.get_attribute('innerHTML')
        soup = BeautifulSoup(div, 'html.parser')
        names.append(soup.find("span", {"class": "content-title ellipsise"}).getText())
    return [(name, link, True) for name, link in zip(names, links)]


def find_show(browser):
    # Finding Show Links
    try:
        src = WebDriverWait(browser, 2).until(
            ec.presence_of_all_elements_located((By.XPATH, "//article[@class='ripple show-card normal']"))
        )
        links = [s.find_element_by_tag_name('a').get_attribute('href') for s in src]
    except TimeoutException:
        return None

    # Finding Show Names
    names = []
    for divs in src:
        div = divs.get_attribute('innerHTML')
        soup = BeautifulSoup(div, 'html.parser')
        names.append(soup.find("span", {"class": "content-title ellipsise"}).getText())
    return [(name, link, False) for name, link in zip(names, links)]


if __name__ == "__main__":
    browser = webdriver.Chrome()
    print(hotstar_search("manmar", browser))