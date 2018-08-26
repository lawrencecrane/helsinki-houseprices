from selenium import webdriver
from bs4 import BeautifulSoup
from oikotie import parse_pages


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

def insert_to_db(data, host):
    print(data)

if __name__ == '__main__':
    for x in parse_pages(page_source):
        insert_to_db(x, "localhost")
