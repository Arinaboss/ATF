import pytest
from Pages.seazonvar import Seazonvar
from Pages.lokators import SeazonvarLocators
from selenium import webdriver


link = "http://seasonvar.ru/"
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


@pytest.mark.parametrize('serial, quantity', [('ходячие мертвецы', '3'),
                                              ('сверхъестественное', '2'),
                                              ('теория большого взрыва', '1'),
                                              ('засланец', '1'),
                                              ('сплетница', '2'),
                                              ('как избежать наказания за убийство', '1')])
def test_search_series_in_website(serial, quantity):
    global browser
    page = Seazonvar(browser, link)
    page.search_series(serial)
    page.page_search(quantity)


@pytest.mark.parametrize('not_serial, zero', [('123456789', '0'),
                                            ('@!#$%^', '0'),
                                            ('jcnhst rjpshmrb', '0'),
                                            ('острые казырьки', '0'),
                                            (' ', '0')])
def test_negativ(not_serial, zero):
    global browser
    page = Seazonvar(browser, link)
    page.search_series(not_serial)
    page.page_search(zero)


def test_registration_in_sait():
    global browser
    page = Seazonvar(browser, link)
    page.login_button()
    page.registration_button()