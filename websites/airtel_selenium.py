from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
# import re


def airtel_search(name, browser, type=None):
    # cleaned_movie_name = re.sub(r'([^\s\w]|_)+', '', movie_name)
    # cleaned_movie_name = cleaned_movie_name.replace(' ', '-')

    # Movies
    if type == "movie":
        browser.get(f'https://www.airtelxstream.in/search/list/movies?category=movie&query={name}')
        return find_movie(browser)

    # TV Show
    elif type == "tv_show":
        browser.get(f'https://www.airtelxstream.in/search/list/tv-shows?category=tvshow&query={name}')
        return find_show(browser)

    # type=None
    else:
        browser.get(f'https://www.airtelxstream.in/search/list/movies?category=movie&query={name}')
        movie = find_movie(browser)
        browser.get(f'https://www.airtelxstream.in/search/list/tv-shows?category=tvshow&query={name}')
        show = find_show(browser)
        if movie and show:
            return movie + show
        elif movie:
            return movie
        elif show:
            return show
        else:
            return None


def find_movie(browser):
    try:
        links = WebDriverWait(browser, 2).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='cards cards-portrait cards-portrait--grid cards-portrait--grid-large']/a")
            )
        )
        movies = [link.get_attribute('href') for link in links]
        title = browser.find_elements_by_xpath("//h5[@class='title']")
        titles = [t.get_attribute("innerText") for i, t in enumerate(title) if i % 2 == 0]
        if len(movies) != len(titles):
            raise Exception("Movies and Titles do not match..")
    except TimeoutException or NoSuchElementException:
        return None
    return [(title, movie, True) for title, movie in zip(titles, movies)]


def find_show(browser):
    try:
        links = WebDriverWait(browser, 2).until(
            ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='cards cards-landscape cards-landscape-grid cards-landscape-grid--large']/a")
            )
        )
        shows = [link.get_attribute('href') for link in links]
        title = browser.find_elements_by_xpath("//h5[@class='title']")
        titles = [t.get_attribute("innerText") for i, t in enumerate(title) if i % 2 == 0]
        if len(shows) != len(titles):
            raise Exception("Shows and Titles do not match..")
    except TimeoutException or NoSuchElementException:
        return None
    return [(title, show, False) for title, show in zip(titles, shows)]


if __name__ == "__main__":
    browser = webdriver.Chrome()
    print(airtel_search("bala", browser))