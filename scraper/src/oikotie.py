from bs4 import BeautifulSoup
from scrape_utilities import safe_get


def transform_data(x):
    # Get all the  data in here
    # we cannot actually open the url of the ad as oikotie is blocking selenium
    # need to configure it differently to do that...
    data = {}
    data['url'] = safe_get(x.find('a'), 'href')

    return data


def process_page(soup, transform_card):
    div_cards = soup.find('div', attrs={"class": "cards"})
    xs = div_cards.find_all('card')

    if (len(xs) == 0):
        return False, None

    return True, [transform_card(x) for x in xs]


def parse_pages(page_source):
    oikotie_url = "https://asunnot.oikotie.fi/vuokrattavat-asunnot?cardType=101&locations=%5B%5B64,6,%22Helsinki%22%5D%5D&pagination="
    page_number = 54
    result = True
    while result:
        result, data = process_page(page_source(oikotie_url + str(page_number)), transform_data)
        yield data
        page_number += 1
