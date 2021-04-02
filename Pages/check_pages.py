from Pages.locators import StoreLokators
from selenium.webdriver.common.action_chains import ActionChains




class Pages():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def login_perseya(self):
        button_login = self.browser.find_element(*StoreLokators.BUTTON_LOGIN)
        button_login.click()

    def page_login(self):
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

    def check_cart(self):
        cart = self.browser.find_element(*StoreLokators.CART)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", cart)
        cart.click()
        prise = "$50.99"
        cena = self.browser.find_element(*StoreLokators.PRICE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", cena)
        assert prise in cena.text, f"expect {'$50,99'} got {cena}"

    def exit(self):
        button_exit = self.browser.find_element(*StoreLokators.EXIT)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", button_exit)
        button_exit.click()

    def login(self):
        button_login = self.browser.find_element(*StoreLokators.BUTTON_LOGIN)
        button_login.click()

    def second_login(self):
        email = self.browser.find_element(*StoreLokators.EMAIL)
        email.click()
        email.send_keys("Perseya@tut.by")
        password = self.browser.find_element(*StoreLokators.PASSW)
        password.click()
        password.send_keys('123456789')
        login = self.browser.find_element(*StoreLokators.L_BUTTON)
        login.click()

    def cart(self):
        cart = self.browser.find_element(*StoreLokators.CART)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", cart)
        cart.click()
        prise = "$27.00"
        cena = self.browser.find_element(*StoreLokators.PRICE)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", cena)
        assert prise in cena.text, f"expect {'$50,99'} got {cena}"