from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def get_html(driver, url):
    driver.get(url)
    return driver.page_source


def safe_get(x, attr):
    if x is None:
        return None

    return x.get(attr)


def create_driver():
    return webdriver.Remote(
        command_executor='http://seleniumserver:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
