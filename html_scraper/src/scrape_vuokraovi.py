import scraper
from functools import reduce
from bs4 import BeautifulSoup


def scrape_ads_from_first_page(ad_callback):
    driver = scraper.create_driver()

    try:
        scrape_ads(driver, ad_callback, 1, 1)
    finally:
        driver.close()


def scrape_ads_from_start_to_last_page(ad_callback, start_page=1):
    driver = scraper.create_driver()

    try:
        page = get_page(driver, 1)
        end_page = min(get_max_pagenumber(page), 100)

        if end_page < start_page:
            raise StartEndError

        scrape_ads(driver, ad_callback, start_page, end_page)
    finally:
        driver.close()


def scrape_ads(driver, ad_callback, start_page=1, end_page=1):
    scraper.do_all_urls(driver,
                        get_all_urls(driver, start_page, end_page),
                        ad_callback)


def get_all_urls(driver, start_page=1, end_page=1):
    return reduce(lambda acc, xs: acc + xs,
                  [get_urls_from_page(driver, page_number)
                   for page_number in range(start_page, end_page)])


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


class StartEndError(Exception):
    pass
