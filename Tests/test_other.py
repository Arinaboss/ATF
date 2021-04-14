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


def test_delite_cart():
    page = Cart(browser, link)
    page.login()
    page.data()
    page.add_product()
    page.cart()

def test_search_dress():
    page = SearchSait(browser, link)
    page.login_in_sait()
    page.input_email("Perseya@tut.by")
    page.input_password('123456789')
    page.search_dress('Printed Dress')
    page.page_search()

def test_speed_navigation():
    page = SearchSait(browser, link)
    page.login_in_sait()
    page.input_email("Perseya@tut.by")
    page.input_password('123456789')
    page.speed_navigation()
    page.result_search()

def test_shopping():
    page = Shopping(browser, link)
    page.login_perseya()
    page.input_email("Perseya@tut.by")
    page.input_password('123456789')
    page.search_dress()
    page.add_dress_in_cart()
    page.window_add()
    page.my_cart()
    page.address()
    page.shipping()
    page.choise_of_payment()
    page.confirm()
    page.order_completed()

def test_mini_cart():
    page = MiniCart(browser, link)
    page.add_product_in_cart()
    page.window_cart()
    page.check_cart()




