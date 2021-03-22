from Pages.lokators import SeazonvarLocators
import time



class Seazonvar():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        #browser.get(self.url)

    def search_series(self):
        box_search = self.browser.find_element(*SeazonvarLocators.BOX)
        box_search.click()
        box_search.send_keys('ходячие мертвецы')
        button = self.browser.find_element(*SeazonvarLocators.BUTTON)
        button.click()

    def page_search(self):
        search = self.browser.find_element(*SeazonvarLocators.RESULTS_SEARCH)
        assert search.is_displayed() == True, f"expect {'result search'} got {'none'}"

    def login_button(self, browser):
        login_click = browser.find_element(*SeazonvarLocators.BUTTON_LOGIN_IN_SAIT)
        login_click.click()
        block_login = browser.find_element(*SeazonvarLocators.BLOCK_LOGIN)
        assert block_login.is_displayed() == True, f"expect {'block_login'} got {'none'}"
