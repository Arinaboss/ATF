from Pages.lokators import StoreLokators
from selenium.webdriver.common.action_chains import ActionChains
import time


class Shopping():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def login_perseya(self):
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

    def search_dress(self):
        woman_menu = self.browser.find_element(*StoreLokators.WOMAN_MENU)
        hov = ActionChains(self.browser).move_to_element(woman_menu)
        hov.perform()
        time.sleep(2)
        casual_dress = self.browser.find_element(*StoreLokators.CASUAL_DRESS)
        casual_dress.click()

    def add_dress_in_cart(self):
        dress = self.browser.find_element(*StoreLokators.NAVIGATION)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", dress)
        hov = ActionChains(self.browser).move_to_element(dress)
        hov.perform()
        add = self.browser.find_element(*StoreLokators.ADD_IN_CART)
        add.click()

    def window_add(self):
        check = self.browser.find_element(*StoreLokators.CHECK_OUT)
        check.click()

    def my_cart(self):
        button_buy = self.browser.find_element(*StoreLokators.BUTTON_BUY)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button_buy)
        button_buy.click()

    def address(self):
        proceed = self.browser.find_element(*StoreLokators.PROCEED)
        proceed.click()

    def shipping(self):
        checkbox = self.browser.find_element(*StoreLokators.CHECKBOX)
        checkbox.click()
        button_proceed = self.browser.find_element(*StoreLokators.SHIPPING)
        button_proceed.click()

    def choise_of_payment(self):
        bank = self.browser.find_element(*StoreLokators.BANK)
        bank.click()

    def confirm(self):
        button = self.browser.find_element(*StoreLokators.CONFIRM)
        button.click()

    def order_completed(self):
        done = self.browser.find_element(*StoreLokators.DONE)
        assert done.is_displayed() == True, f"expect{'yes'} got {'error'}"




