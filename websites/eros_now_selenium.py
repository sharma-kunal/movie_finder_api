from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver


def eros_search(name, browser, typ=None):

    # Movies
    if typ == "movies":
        browser.get(f'https://erosnow.com/search/movies/{name}')
        return find_movie(browser)

    # TV Shows
    elif typ == "tv_shows":
        browser.get(f'https://erosnow.com/search/tvshow/{name}')
        return find_show(browser)

    # typ = 'None'
    else:
        browser.get(f'https://erosnow.com/search/movies/{name}')
        movies = find_movie(browser)
        browser.get(f'https://erosnow.com/search/tvshow/{name}')
        shows = find_show(browser)
        if movies and shows:
            return movies + shows
        elif movies:
            return movies
        elif shows:
            return shows
        else:
            return None


def find_movie(browser):
    try:
        links = WebDriverWait(browser, 2).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//div[@class='m-box']/a"))
        )
        movies = [link.get_attribute('href') for link in links]
        title = browser.find_elements_by_xpath("//h4[@class='m-box-title ellipsis']")
        titles = [t.get_attribute("innerText") for t in title]
        if len(movies) != len(titles):
            raise Exception("Movies and Titles do not match")
    except TimeoutException or NoSuchElementException:
        return None
    return [(title, movie, True) for title, movie in zip(titles, movies)]


def find_show(browser):
    try:
        links = WebDriverWait(browser, 2).until(
            ec.presence_of_all_elements_located((By.XPATH,
                                                 "//div[@class='h-box eros-box']/a"))
        )
        shows = [link.get_attribute('href') for link in links]
        title = browser.find_elements_by_xpath("//span[@class='h-box-heading ellipsis']")
        titles = [t.get_attribute("innerText") for t in title]
        if len(shows) != len(titles):
            raise Exception("Movies and Titles do not match")
    except TimeoutException or NoSuchElementException:
        return None
    return [(title, show, False) for title, show in zip(titles, shows)]


def find_originals(browser):
    # cant find in originals as there is no name avaliable
    return None


if __name__ == "__main__":
    browser = webdriver.Firefox()
    print(eros_search("badla", browser))