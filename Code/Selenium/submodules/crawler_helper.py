import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options


def wait_for_load(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 20:
            print('Timing out after 10 seconds and returning')
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return


def chrome_headless_mode_initialization():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless")
    # chrome_options.headless = True # also works
    return chrome_options

def firefox_headless_mode_initialization():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-dev-shm-usage')
    return firefox_options

def page_form_extract(driver):
    form = driver.find_element_by_id('announcementList').text
    return form
