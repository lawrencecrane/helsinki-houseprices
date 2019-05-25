import scraper
from functools import reduce
from bs4 import BeautifulSoup


def scrape_ads(ad_callback):
    driver = scraper.create_driver()

    scraper.do_all_urls(driver,
                        get_all_urls(driver),
                        ad_callback)


def get_all_urls(driver):
    page = get_page(driver, 1)
    last_page = min(get_max_pagenumber(page), 100)

    return reduce(lambda a, b: a + b,
                  [get_urls_from_page(driver, page_number)
                   for page_number in range(1, last_page)])


def get_urls_from_page(driver, page_number):
    page = get_page(driver, page_number)

    list_content = page.find('div', attrs={'id': 'listContent'})
    ads = list_content.find_all('div', attrs={'class': 'list-item-container'})

    urls = [get_url(ad) for ad in ads]

    return ['https://www.vuokraovi.com' + url
            for url in urls
            if url is not None]


def get_url(ad):
    return scraper.safe_get(ad.find('a', attrs={"class": "list-item-link"}),
                            'href')


def get_page(driver, page_number):
    url = 'https://www.vuokraovi.com/vuokra-asunnot/Helsinki?pageType=list&page='
    return BeautifulSoup(scraper.get_html(driver, url + str(page_number)),
                         'html.parser')


def get_max_pagenumber(page):
    lis = page.find('ul', attrs={'class': 'pagination'}).find_all('li')
    return int(lis[len(lis)-2].text)
