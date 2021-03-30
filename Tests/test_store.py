from Pages.clothing_store import Store
import pytest
from selenium import webdriver
from Pages.registration_perseya import Perseya


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

def test_input_mail():
    global browser
    page = Store(browser, link)
    page.login_new_user()
    page.registration_new_user()
    page.registration_field()

def test_registration_perseya():
    global browser
    page = Perseya(browser, link)
    page.login_perseya()
    page.registration_perseya()
    page.registration_perseya_continuation()




