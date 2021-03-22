from selenium import webdriver
from selenium.webdriver.common.by import By



class Iphone():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(url)

    def search(self, browser):
        search_box = browser.find_element(By.CSS_SELECTOR, ".fast-search__input")
        search_box.click()
        search_box.send_keys("iphone 12 pro")

    def image(self, browser):
        photo = browser.find_element(By.CSS_SELECTOR, ".result__wrapper :nth-child(3) img")
        assert photo.is_displayed() == True, f"expect {photo} got {'blank screen'}"

    def link_to_product(self, browser):
        product = browser.find_element(By.XPATH, "//*[text()='Смартфон Apple iPhone 12 Pro 128GB (графитовый)']")
        assert product.is_displayed() == True, f"expect {product} got {'empty field'}"

    def description(self, browser):
        description_product = browser.find_element(By.XPATH, "//a[text()='Apple iOS, экран 6.1' OLED (1170x2532), Apple A14 Bionic, ОЗУ 6 ГБ, флэш-память 128 ГБ, камера 12 Мп, аккумулятор 2775 мАч, '1 SIM']")
        assert description_product.is_displayed() == True, f"expect {description_product} got {'empty field'}"

    def price(self, browser):
        price_phone = browser.find_element(By.CSS_SELECTOR, "[data-bind='html: $root.format.minPrice($data.prices, 'BYN')']")
        assert price_phone.is_displayed() == True, f"expect{price_phone.text} got {'empty field'}"



