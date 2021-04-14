from Pages.lokators import StoreLokators
from selenium.webdriver.common.action_chains import ActionChains
import time


class MiniCart():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def add_product_in_cart(self):
        dress = self.browser.find_element(*StoreLokators.BOX_BLACK_BLOUSES)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", dress)
        hov = ActionChains(self.browser).move_to_element(dress)
        hov.perform()
        button_add = self.browser.find_element(*StoreLokators.BLACK_BLOUSES)
        button_add.click()
        continue_shopping = self.browser.find_element(*StoreLokators.CUNT_SHOPPING)
        continue_shopping.click()
        printed_dress = self.browser.find_element(*StoreLokators.PRINTED_DRESS)
        hov = ActionChains(self.browser).move_to_element(printed_dress)
        hov.perform()
        add_dress = self.browser.find_element(*StoreLokators.PRINTED_ADD)
        add_dress.click()
        cont = self.browser.find_element(*StoreLokators.CUNT_SHOPPING)
        cont.click()
        white_black_dress = self.browser.find_element(*StoreLokators.WHITE_BLACK_DRESS)
        hov = ActionChains(self.browser).move_to_element(white_black_dress)
        hov.perform()
        wbd_add = self.browser.find_element(*StoreLokators.WBD_ADD)
        wbd_add.click()
        shopping = self.browser.find_element(*StoreLokators.CUNT_SHOPPING)
        shopping.click()

    def window_cart(self):
        cart = self.browser.find_element(*StoreLokators.CART)
        hov = ActionChains(self.browser).move_to_element(cart)
        hov.perform()
        time.sleep(2)
        mini_del = self.browser.find_element(*StoreLokators.MINI_DEL)
        mini_del.click()
        time.sleep(3)
        del_blouses = self.browser.find_element(*StoreLokators.DEL_BLUES)
        del_blouses.click()
        time.sleep(3)
        check = self.browser.find_element(*StoreLokators.CHECK)
        check.click()

    def check_cart(self):
        quantity = self.browser.find_element(*StoreLokators.QUANTITY)
        my_quantity = "1"
        assert my_quantity in quantity.text, f"expect{'1'} got {'hz'}"

