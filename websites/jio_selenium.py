from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://www.jiocinema.com"


def jio_search(name, browser, typ=None):
    # Search Movies
    if typ == "movie":
        print("finding page")
        browser.get(f"https://www.jiocinema.com/search/{name}/Movies")
        page = remove_add(browser)
        # closing the ad
        # x = browser.find_elements_by_tag_name('body')
        # print(len(x))
        # browser.find_element_by_xpath("//span[@class='CT_InterstitialClose']").click()
        print("finding movie")
        return find_movie(page)

    # TV Show
    elif typ == "tv_show":
        try:
            browser.set_page_load_timeout(4)
            browser.get(f"https://www.jiocinema.com/search/{name}/TV Shows")
            page = remove_add(browser)
        except Exception:
            return None
        return find_show(page)

    # typ = 'None'
    else:
        try:
            print(0)
            browser.set_page_load_timeout(4)
            browser.get(f"https://www.jiocinema.com/search/{name}/Movies")
            print(0.5)
            page = remove_add(browser)
            movies = find_movie(page)
            print(1)
        except Exception:
            movies = []
        try:
            print(2)
            browser.set_page_load_timeout(4)
            browser.get(f"https://www.jiocinema.com/search/{name}/TV Shows")
            print(1.5)
            page = remove_add(browser)
            shows = find_show(page)
            print(3)
        except Exception:
            shows = []
        if movies and shows:
            print(4)
            return movies + shows
        elif movies:
            print(5)
            return movies
        elif shows:
            print(6)
            return shows
        else:
            print(7)
            return None


def remove_add(page):
    try:
        iframe = WebDriverWait(browser, 5).until(
            ec.presence_of_element_located((By.XPATH, "//iframe"))
        )
        browser.switch_to.frame(iframe)
        browser.find_element_by_xpath("//span[@class='CT_InterstitialClose']").click()
        browser.switch_to.parent_frame()
        return browser.find_element_by_tag_name("body").get_attribute("innerHTML")
    except Exception or NoSuchElementException or TimeoutException as e:
        return browser.find_element_by_tag_name("body").get_attribute("innerHTML")


def find_movie(browser):
    try:
        temp = WebDriverWait(browser, 5).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='row carousel-container']"))
        )
    except:
        time.sleep(4)
    try:
        soup = BeautifulSoup(browser, 'html.parser')
        row = soup.find("div", {"class": "row carousel-container"})
        result = []
        print("row found")
        movies = row.find_all("div", {"class": "carouselItem"})
        print("movies found")
        try:
            movies = movies[:6]
        except IndexError:
            pass
        for data in movies:
            link = url + data.find("a")['href']
            name = data.find("img")['itemname']
            result.append((name, link, True))
        return result
    except Exception or NoSuchElementException or TimeoutException as e:
        print("movie not found")
        print(e)
        return None


def find_show(browser):
    try:
        soup = BeautifulSoup(browser, 'html.parser')
        row = soup.find("div", {"class": "row carousel-container"})
        result = []
        shows = row.find_all("div", {"class": "carouselItem"})
        try:
            shows = shows[:6]
        except IndexError:
            pass
        for data in shows:
            link = url + data.find("a")['href']
            name = data.find("img")['itemname']
            result.append((name, link, False))
        return result
    except Exception or NoSuchElementException or TimeoutException as e:
        print("show cant be found")
        print(e)
        return None


if __name__ == "__main__":
    # options = Options()
    # options.headless = True
    browser = webdriver.Chrome()
    print(jio_search("boss", browser, "movie"))