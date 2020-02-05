from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
import time

failure_counter = 0


def idea_search(name, browser):
    global failure_counter
    browser.get("https://www.ideamoviesandtv.in/")
    browser.get(f"https://www.ideamoviesandtv.in/Searchresults?query={name}")
    try:
        src = WebDriverWait(browser, 3).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='flex-container']"))
        )
    except TimeoutException:
        failure_counter += 1
        if failure_counter == 2:
            return None
        idea_search(name, browser)
    # selenium is unable to scrape this fast so 1 sec pause
    time.sleep(1)
    divs = browser.find_elements_by_xpath("//div[@class='flex-dev']/a")
    names = browser.find_elements_by_xpath("//div[@class='episodes-info']/span")
    print(len(divs), len(names))
    if len(divs) != len(names)//2:
        print(len(divs), len(names))
        raise Exception("Movies and Names do not match")
    return find_movie_and_show([d.get_attribute('href') for d in divs],
                               [name.get_attribute('innerText') for i, name in enumerate(names) if i % 2 == 0]) or None


def find_movie_and_show(links, names):
    result = []
    for i, link in enumerate(links):
        if "movies" in link[31:]:
            result.append((names[i], link, True))
        elif "tvshows" in link[31:]:
            result.append((names[i], link, False))
    return result


if __name__ == "__main__":
    browser = webdriver.Chrome()
    print(idea_search("ma", browser))
