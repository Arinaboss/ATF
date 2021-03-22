from Pages.lokators import CatalogLokators
import time

class Catalog():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(url)

    def catalog_link(self, browser):
        link = browser.find_element(*CatalogLokators.CATALOG)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", link)
        assert link.is_displayed() == True, f"expect {'catalog'} got {'none'}"

    def catalog_open(self, browser):
        catalog = browser.find_element(*CatalogLokators.CATALOG)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", catalog)
        catalog.click()

    def block_catalog(self, browser):
        block = browser.find_element(*CatalogLokators.CATALOG_BLOCK)
        assert block.is_displayed() == True, f"expect {'block'} got {'none'}"

    def open_block(self, browser):
        home = browser.find_element(*CatalogLokators.CATALOG_HOME)
        home.click()
        assert home.is_displayed() == True, f"expect {'menu'} got {'none'}"

    def open_main(self, browser):
        browser.back()

    def info_catalog(self, browser):
        info = browser.find_element(*CatalogLokators.INFO_BOX)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", info)
        assert info.is_displayed() == True, f"expect {'info'} got {'none'}"

    def open_hp(self, browser):
        hp = browser.find_element(*CatalogLokators.HP_BOX)
        hp.click()

    def hp(self, browser):
        name = browser.find_element(*CatalogLokators.PAGE_HP)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", name)
        assert name.is_displayed() == True, f"expect {'name info'} got {'none'}"

    def image_hp(self, browser):
        image = browser.find_element(*CatalogLokators.IMAGE_HP)
        assert image.is_displayed() == True, f"expect {'image'} got {'none'}"

    def text_hp(self, browser):
        text = browser.find_element(*CatalogLokators.TEXT_PAGE)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", text)
        assert text.is_displayed() == True, f"expect {'text'} got {'none'}"

    def click_back(self, browser):
        browser.back()

    def product_box(self, browser):
        box = browser.find_element(*CatalogLokators.PRODUCT_BOX)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", box)
        assert box.is_displayed() == True, f"expect {'product'} got {'none'}"

    def open_pizza(self, browser):
        pizza = browser.find_element(*CatalogLokators.PIZZA)
        pizza.click()

    def name_pizza(self, browser):
        name = browser.find_element(*CatalogLokators.NAME_PIZZA)
        assert name.is_displayed() == True, f"expect {'name'} got {'none'}"

    def image_pizza(self, browser):
        image = browser.find_element(*CatalogLokators.IMG_PIZZA)
        time.sleep(3)
        assert image.is_displayed() == True, f"expect {'image'} got {'none'}"

    def text_pizza(self, browser):
        text = browser.find_element(*CatalogLokators.TEXT_PIZZA)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", text)
        time.sleep(2)
        assert text.is_displayed() == True, f"expect {'text'} got {'none'}"

