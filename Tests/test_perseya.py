from selenium import webdriver
from Pages.perseya_pages import PagesPerseya
import pytest
import time
from Pages.check_pages import Pages


link = "http://automationpractice.com/index.php"
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


def test_login_perseya():
    page = PagesPerseya(browser, link)
    page.entrance()
    page.login_page()
    page.adding_in_cart()
    page.check_cart()


def test_perseya_pages():
    page = Pages(browser, link)
    page.login_perseya()
    page.page_login()
    page.add_product()
    page.check_cart()
    page.exit()
    page.login()
    page.second_login()
    page.cart()



