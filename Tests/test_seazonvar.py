import pytest
from Pages.seazonvar import Seazonvar
from Pages.lokators import SeazonvarLocators
from selenium import webdriver


link = "http://seasonvar.ru/"
browser = None


@pytest.fixture(scope="function")
def before():
    global browser
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

#@pytest.mark.parametrize('serial', ['ходячие мертвецы',
#                                    'сверхъестественное',
#                                    'теория большого взрыва',
#                                    'засланец',
#                                    'сплетница',
#                                    'как избежать наказания за убийство'])
def test_search_series_in_website():
    global browser
    page = Seazonvar(browser, link)
    page.search_series()
    page.page_search()

