from Pages.locators import RateLokators

class Rate():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(self.url)

    def rate_box(self, browser):
        box = browser.find_element(*RateLokators.CURRENCY)
        assert box.is_displayed() == True, f"expect {'rate'} got {'none'}"

    def ope_page(self, browser):
        box = browser.find_element(*RateLokators.CURRENCY)
        box.click()

    def table_carrency(self, browser):
        table = browser.find_element(*RateLokators.TABLE_CURRENCY)
        assert table.is_displayed() == True, f"expect {'table'} got {'none'}"

