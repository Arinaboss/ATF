from Pages.locators import SeazonvarLocators
import time



class Seazonvar():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        #browser.get(self.url)

    def search_series(self, word):
        box_search = self.browser.find_element(*SeazonvarLocators.BOX)
        box_search.click()
        box_search.send_keys(word)
        button = self.browser.find_element(*SeazonvarLocators.BUTTON)
        button.click()

    def page_search(self, quantity):
        search = self.browser.find_element(*SeazonvarLocators.RESULTS_SEARCH)
        result = quantity
        time.sleep(2)
        assert result in search.text, f"expect {'result search'} got {'none'}"

    def login_button(self):
        login_click = self.browser.find_element(*SeazonvarLocators.BUTTON_LOGIN_IN_SAIT)
        login_click.click()
        blok_login = self.browser.find_element(*SeazonvarLocators.BLOCK_LOGIN)
        assert blok_login.is_displayed() == True, f"expect {'block_login'} got {'none'}"

    def registration_button(self):
        button = self.browser.find_element(*SeazonvarLocators.BUTTON_REGISTRATION)
        button.click()
        block_registration = self.browser.find_element(*SeazonvarLocators.BLOCK_REGISTRATION)
        assert block_registration.is_displayed() == True
