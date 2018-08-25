from selenium import webdriver
from bs4 import BeautifulSoup

oikotie_url = "https://asunnot.oikotie.fi/vuokrattavat-asunnot?cardType=101&locations=%5B%5B64,6,%22Helsinki%22%5D%5D"

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

def parse_oikotie_page(soup):
    house_urls = []
    # Get element: <div class="cards"></div>
    # This contains all the houses in the page
    cards = soup.find('div', attrs={"class": "cards"})
    return cards
    #next_page = ""
    #return house_urls, next_page

if __name__ == '__main__':
    print(parse_oikotie_page(get_page(oikotie_url)))

