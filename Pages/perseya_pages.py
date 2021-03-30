from Pages.lokators import StoreLokators
from selenium.webdriver.common.action_chains import ActionChains



class PagesPerseya():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(url)

    def entrance(self):
        button_login = self.browser.find_element(*StoreLokators.BUTTON_LOGIN)
        button_login.click()

    def login_page(self):
        email = self.browser.find_element(*StoreLokators.EMAIL)
        email.click()
        email.send_keys("Perseya@tut.by")
        password = self.browser.find_element(*StoreLokators.PASSW)
        password.click()
        password.send_keys('123456789')
        login = self.browser.find_element(*StoreLokators.L_BUTTON)
        login.click()
        account = self.browser.find_element(*StoreLokators.WELCOME)
        assert account.is_displayed() == True


    def adding_in_cart(self):
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



