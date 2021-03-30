from selenium import webdriver
from selenium.webdriver.common.by import By



class Iphone():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(url)

    def search(self):
        search_box = self.browser.find_element(By.CSS_SELECTOR, ".fast-search__input")
        search_box.click()
        search_box.send_keys("iphone 12 pro")

    def image(self):
        self.browser.switch_to.frame(self.browser.find_element(By.CSS_SELECTOR, '.modal-iframe'))
        photo = self.browser.find_element(By.CSS_SELECTOR,
                                           '[src="//content2.onliner.by/catalog/device/header/01e04bb3519e9f859244d8df82104230.jpeg"]')
        assert photo.is_displayed() == True, f"expect {'photo'} got {'blank screen'}"

    def link_to_product(self):
        product = self.browser.find_element(By.CSS_SELECTOR, '[class="product__details"] [class="product__title"]')
        assert product.is_displayed() == True, f"expect {product} got {'empty field'}"

    def description(self):
        description_product = self.browser.find_element(By.CSS_SELECTOR, '[class="product__description"]')
        assert description_product.is_displayed() == True, f"expect {description_product} got {'empty field'}"

    def price(self):
        price_phone = self.browser.find_element(By.CSS_SELECTOR, '.product__price-value.product__price-value_primary')
        assert price_phone.is_displayed() == True, f"expect{price_phone.text} got {'empty field'}"


    def menu(self):
        block_serch = self.browser.find_element(By.CSS_SELECTOR, '.search__content-wrapper')
        assert block_serch.is_displayed() == True
