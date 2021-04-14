from selenium import webdriver
from Pages.check_delite_cart import Cart
import pytest
import time
from Pages.check_search import SearchSait
from Pages.buying_a_dress import Shopping
from Pages.mini_cart import MiniCart
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


def test_delete_cart():
    page = Cart(browser, link)
    page.login()
    page.data()
    page.add_product()
    page.cart()
