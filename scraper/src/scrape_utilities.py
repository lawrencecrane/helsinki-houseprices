from selenium import webdriver
from bs4 import BeautifulSoup


def page_source(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery");
    options.add_argument("--start-maximized")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        html = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        html = None
    finally:
        driver.quit()

    return html


def safe_get(x, attr):
    if (x == None):
        return None

    return x.get(attr)


def safe_text(x):
    if (x == None):
        return None

    return x.text
