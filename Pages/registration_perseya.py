from Pages.lokators import StoreLokators
import time
from selenium.webdriver.support.ui import Select


class Perseya():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def login_perseya(self):
        button_login = self.browser.find_element(*StoreLokators.BUTTON_LOGIN)
        button_login.click()

    def registration_perseya(self):
        input_mail = self.browser.find_element(*StoreLokators.INPUT_EMAIL)
        input_mail.click()
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", input_mail)
        input_mail.send_keys("Perseya@tut.by")
        create = self.browser.find_element(*StoreLokators.BUTTON_CREATE)
        create.click()

    def registration_perseya_continuation(self):
        name = self.browser.find_element(*StoreLokators.NAME)
        name.click()
        name.send_keys('Perseya')
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", name)
        last_name = self.browser.find_element(*StoreLokators.LAST_NAME)
        last_name.click()
        last_name.send_keys('Lanister')
        password = self.browser.find_element(*StoreLokators.PASSWORD)
        password.click()
        password.send_keys('123456789')
        adress = self.browser.find_element(*StoreLokators.ADRESS)
        adress.click()
        adress.send_keys(str(time.time()))
        city = self.browser.find_element(*StoreLokators.CITY)
        city.click()
        city.send_keys('New York')
        shtat = self.browser.find_element(*StoreLokators.SHTAT)
        shtat.click()
        select = Select(self.browser.find_element_by_name('id_state'))
        select.select_by_value('1')
        post = self.browser.find_element(*StoreLokators.POST)
        post.click()
        post.send_keys('00000')
        phone = self.browser.find_element(*StoreLokators.PHONE)
        phone.click()
        phone.send_keys('+123456789')
        nicname = self.browser.find_element(*StoreLokators.NICNAME)
        nicname.click()
        nicname.clear()
        nicname.send_keys('Мир грез')
        reg = self.browser.find_element(*StoreLokators.REG)
        reg.click()
        welcome = self.browser.find_element(*StoreLokators.WELCOME)
        assert welcome.is_displayed() == True
