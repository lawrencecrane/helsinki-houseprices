from bs4 import BeautifulSoup
from scrape_utilities import safe_get, safe_text, page_source

def parse_key(x):
    x.find('th')

def parse_value(x):
    x.find('td')

def transform_ad_data(x):
    data = {}
    data['latitude'] = safe_get(x.find('meta', attrs={"itemprop": "latitude"}), 'content')
    data['longitude'] = safe_get(x.find('meta', attrs={"itemprop": "longitude"}), 'content')

    rentalContactInfo =  x.find('div', attrs={"id": "rentalContactInfo"})

    if (rentalContactInfo.p.b.a == None):
        data['advertiser'] = safe_text(rentalContactInfo.p.b)
        data['is_private'] = True
    else:
        data['advertiser'] = safe_text(rentalContactInfo.p.b.a)
        data['is_private'] = False

    # basic_info = x.select('#collapseOne table')
    # data.update({parse_key(x): parse_value(x) for x in basic_info.find_all('tr')})

    # cost_info = x.select('#collapseTwo table')
    # data.update({parse_key(x): parse_value(x) for x in cost_info.find_all('tr')})

    return data


def process_ad(url):
    if (url == None):
        return None

    return page_source("https://www.vuokraovi.com" + url)


def get_url(x):
    return safe_get(x.find('a', attrs={"class": "list-item-link"}), 'href')


def process_page(soup, transform_ad):
    ads_html = soup.find('div', attrs={"id": "listContent"})
    ads = ads_html.find_all('div', attrs={"class": "list-item-container"})

    # This wont work for vuokraovi:
    if (len(ads) == 0):
        return False, None

    f = lambda x: transform_ad(process_ad(get_url(x)))
    return True, [f(x) for x in ads]


def scrape_pages():
    url = "https://www.vuokraovi.com/vuokra-asunnot/Helsinki?pageType=list&page="
    page_number = 1
    isData = True
    while isData:
        isData, data = process_page(page_source(url + str(page_number)), transform_ad_data)
        yield data
        page_number += 1
