from Pages.lokators import StoreLokators
from selenium.webdriver.common.action_chains import ActionChains
import time


class SearchSait():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def login_in_sait(self):
        button_login = self.browser.find_element(*StoreLokators.BUTTON_LOGIN)
        button_login.click()

    def input_email(self, key):
        email = self.browser.find_element(*StoreLokators.EMAIL)
        email.click()
        email.send_keys(key)

    def input_password(self, key):
        password = self.browser.find_element(*StoreLokators.PASSW)
        password.click()
        password.send_keys(key)
        login = self.browser.find_element(*StoreLokators.L_BUTTON)
        login.click()

    def search_dress(self, key):
        search = self.browser.find_element(*StoreLokators.SEARCH)
        search.click()
        search.send_keys(key)
        button = self.browser.find_element(*StoreLokators.SEARCH_BUTTON)
        button.click()

    def page_search(self):
        block_search = self.browser.find_element(*StoreLokators.BLOCK_SEARCH)
        assert block_search.is_displayed() == True, f"expect{'yes'} got {'error'}"

    def speed_navigation(self):
        woman_menu = self.browser.find_element(*StoreLokators.WOMAN_MENU)
        hov = ActionChains(self.browser).move_to_element(woman_menu)
        hov.perform()
        time.sleep(2)
        blouses = self.browser.find_element(*StoreLokators.BLOUSES)
        blouses.click()

    def result_search(self):
        product = self.browser.find_element(*StoreLokators.SEARCH_BLOUSES)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", product)
        assert product.is_displayed() == True, f"expect{'yes'} got {'error'}"



