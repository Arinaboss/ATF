import pytest
from selenium import webdriver
from Pages.onliner import Iphone
from Pages.weather import Weather
from Pages.rate import Rate
from Pages.news import News
from Pages.catalog import Catalog
from Pages.seazonvar import Seazonvar
import time


link = "https://www.onliner.by/"
browser = None


@pytest.fixture(autouse=True)
def before():
    global browser
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.get(link)

    yield
    if browser is not None:
        browser.quit()


def test_iphone():
    global browser
    page = Iphone(browser, link)
    page.search()
    page.image()
    page.link_to_product()
    page.description()
    page.price()
    page.menu()


#def test_weather(before):
#    page = Weather(browser, link)
#    time.sleep(3)
#    page.weather_box(browser)
#    page.weather_page(browser)
#    page.weather_today(browser)

#def test_rate(before):
#    page = Rate(browser, link)
#    page.rate_box(browser)
#    time.sleep(2)
#    page.ope_page(browser)
#    page.table_carrency(browser)

#def test_news(before):
#    page = News(browser, link)
#    page.news_box(browser)
#    page.image_in_box(browser)
#    page.name_box_news(browser)
#    page.open_news(browser)
#    page.news_image(browser)
#    page.name_news(browser)
#    page.text_news(browser)

#def test_catalog():
#    page = Catalog(browser, link)
#    page.catalog_link(browser)
#    page.catalog_open(browser)
#    page.block_catalog(browser)
#    page.open_block(browser)
#    page.open_main(browser)
#    page.info_catalog(browser)
#    page.open_hp(browser)
#    page.hp(browser)
#    page.image_hp(browser)
#    page.text_hp(browser)
#    page.click_back(browser)
#    page.product_box(browser)
#    page.open_pizza(browser)
#    page.name_pizza(browser)
#    page.image_pizza(browser)
#    page.text_pizza(browser)

def test_search_series_in_website():
    global browser
    page = Seazonvar(browser, link)
    page.search_series()
    page.page_search()