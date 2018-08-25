from selenium import webdriver
from bs4 import BeautifulSoup


def get_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)

        html = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        html = None
    finally:
        driver.quit()

    return html

def parse_url_from_oikotie_ad(x):
    url = x.find('a').get('href')
    return url

def parse_oikotie_page(soup):
    cards_container = soup.find('div', attrs={"class": "cards"})
    cards = cards_container.find_all('card')

    if (len(cards) == 0):
        house_urls = None
    else:
        house_urls = map(parse_url_from_oikotie_ad, cards)

    return house_urls

def go_through_oikotie_pages():
    oikotie_url = "https://asunnot.oikotie.fi/vuokrattavat-asunnot?cardType=101&locations=%5B%5B64,6,%22Helsinki%22%5D%5D"
    page = "&pagination="
    page_number = 1
    all_urls = []
    while True:
        house_urls = parse_oikotie_page(get_page(oikotie_url + page + str(page_number)))
        if (house_urls == None):
            break

        # map house_urls...
        all_urls += house_urls
        page_number += 1

    return all_urls


if __name__ == '__main__':
    print(go_through_oikotie_pages())
