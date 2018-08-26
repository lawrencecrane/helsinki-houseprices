from bs4 import BeautifulSoup
from scrape_utilities import safe_get, safe_text, page_source


def transform_data(x):
    # Get all the  data in here
    # we cannot actually open the url of the ad as oikotie is blocking selenium
    # need to configure it differently to do that...
    data = {}
    data['url'] = safe_get(x.find('a'), 'href')
    data['address'] = safe_text(x.find('div', attrs={"ng-bind": "$ctrl.card.building.address"}))

    return data


def process_page(soup, transform_ad):
    div_cards = soup.find('div', attrs={"class": "cards"})
    xs = div_cards.find_all('card')

    if (len(xs) == 0):
        return False, None

    return True, [transform_ad(x) for x in xs]


def scrape_pages():
    oikotie_url = "https://asunnot.oikotie.fi/vuokrattavat-asunnot?cardType=101&locations=%5B%5B64,6,%22Helsinki%22%5D%5D&pagination="
    page_number = 1
    isData = True
    while isData:
        isData, data = process_page(page_source(oikotie_url + str(page_number)), transform_data)
        yield data
        page_number += 1
