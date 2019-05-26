import scrape_utils as utils
from functools import reduce
from bs4 import BeautifulSoup


class VuokraoviScraper():
    def __init__(self):
        pass

    def scrape_ads(driver, ad_callback, start_page=1, end_page=1):
        driver.do_all_urls(
            VuokraoviScraper.get_all_urls(driver, start_page, end_page),
            ad_callback
        )

    def get_all_urls(driver, start_page=1, end_page=1):
        urls = [VuokraoviParser.get_urls_from_page(driver.get_page(page))
                for page in range(start_page, end_page + 1)]

        return reduce(lambda acc, xs: acc + xs, urls)


class VuokraoviDriver():
    def __init__(self, url):
        self.url = url
        self.query = url + '/vuokra-asunnot/Helsinki?pageType=list&page='

    def __enter__(self):
        self.driver = utils.create_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()

    def get_page(self, page_number):
        return BeautifulSoup(utils.get_html(self.driver,
                                            self.query + str(page_number)),
                             'html.parser')

    def do_all_urls(self, urls, callback):
        for url in urls:
            abs_url = self.url + url
            html = utils.get_html(self.driver, abs_url)
            callback(abs_url, html)


class VuokraoviParser():
    def __init__(self):
        pass

    def get_urls_from_page(page):
        list_content = page.find('div', attrs={'id': 'listContent'})

        ads = list_content.find_all('div',
                                    attrs={'class': 'list-item-container'})

        return [url for url in
                [VuokraoviParser.get_url_from_ad(ad) for ad in ads]
                if url is not None]

    def get_url_from_ad(ad):
        return utils.safe_get(ad.find('a', attrs={"class": "list-item-link"}),
                              'href')

    def get_max_pagenumber(page):
        lis = page.find('ul', attrs={'class': 'pagination'}).find_all('li')
        return int(lis[len(lis)-2].text)
