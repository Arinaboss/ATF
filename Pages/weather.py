from Pages.locators import WeatherLokators
import time


class Weather():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(self.url)

    def weather_box(self, browser):
        box = browser.find_element(*WeatherLokators.BOX)
        assert box.is_displayed() == True, f"expect {box} got {'none'}"

    def weather_page(self, browser):
        box = browser.find_element(*WeatherLokators.BOX)
        box.click()

    def weather_today(self, browser):
        box = browser.find_element(*WeatherLokators.TODAY)
        assert box.is_displayed() == True, f"expect {box} got {'none'}"



