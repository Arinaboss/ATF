from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.locators import StoreLokators
from selenium.webdriver.common.action_chains import ActionChains
import time


class Cart:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def login(self):
        button_login = self.browser.find_element(*StoreLokators.BUTTON_LOGIN)
        button_login.click()

    def data(self):
        email = self.browser.find_element(*StoreLokators.EMAIL)
        email.click()
        email.send_keys("Perseya@tut.by")
        password = self.browser.find_element(*StoreLokators.PASSW)
        password.click()
        password.send_keys('123456789')
        login = self.browser.find_element(*StoreLokators.L_BUTTON)
        login.click()

    def add_product(self):
        dress = self.browser.find_element(*StoreLokators.DRESS)
        dress.click()
        model = self.browser.find_element(*StoreLokators.MODEL)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", model)
        hov = ActionChains(self.browser).move_to_element(model)
        hov.perform()
        add = self.browser.find_element(*StoreLokators.ADD)
        add.click()
        clouse = self.browser.find_element(*StoreLokators.CLOUSE_WINDOW)
        clouse.click()

    def cart(self):
        cart = self.browser.find_element(*StoreLokators.CART)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", cart)
        cart.click()
        delete = self.browser.find_element(*StoreLokators.DELETE_BUTTON)
        delete.click()
        self.wait_el(StoreLokators.MESSAGE)
        message = self.browser.find_element(*StoreLokators.MESSAGE)
        assert message.is_displayed(), f"expect your cart empty got ne-a"


    def wait_element(self, locator):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        wait = WebDriverWait(self.browser, 15, ignored_exceptions=ignored_exceptions)
        located = expected_conditions.visibility_of_element_located(locator)
        wait.until(located)
