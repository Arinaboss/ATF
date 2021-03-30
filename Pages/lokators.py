from selenium.webdriver.common.by import By

class WeatherLokators():
    BOX = (By.CSS_SELECTOR, "[href='https://pogoda.onliner.by/']")
    TODAY = (By.CSS_SELECTOR, ".b-weather-today__actual")

class RateLokators():
    CURRENCY = (By.CSS_SELECTOR, "[href='https://kurs.onliner.by/']")
    TABLE_CURRENCY = (By.CSS_SELECTOR, ".b-currency-table")

class NewsLokators():
    NEWS_BOX = (By.XPATH, '//*[@id="widget-111"]')
    NAME_BOX = (By.XPATH, '//*[text()="Самые дорогие картины на Netflix и других стриминг-сервисах"]')
    IMAGE_IN_BOX = (By.CSS_SELECTOR, '[style="background-image:url(https://content.onliner.by/widget/news/1x1/9a51a67a504315831932470538ed309b.jpeg)"]')
    IMAGE_NEWS = (By.CSS_SELECTOR, ".news-header__image")
    NEWS_NAME = (By.CSS_SELECTOR, ".news-header__top h1")
    TEXT_NEWS = (By.CSS_SELECTOR, ".news-entry__speech p")

class CatalogLokators():
    CATALOG = (By.XPATH, "//h2/a")
    CATALOG_BLOCK = (By.CSS_SELECTOR, ".catalog-navigation-classifier")
    CATALOG_HOME = (By.CSS_SELECTOR, '[class="catalog-navigation-classifier__item "][data-id="5"]')
    HOME_MENU = (By.CSS_SELECTOR, '[class="catalog-navigation-list  catalog-navigation-list_active catalog-navigation-list_opened"]')
    INFO_BOX = (By.CSS_SELECTOR, ".b-catalog-layer")
    HP_BOX = (By.XPATH, '//div[@class="b-tiles cfix"]/div[3]')
    PAGE_HP = (By.CSS_SELECTOR, ".news-header__preview h1")
    IMAGE_HP = (By.CSS_SELECTOR, ".news-header__image")
    TEXT_PAGE = (By.CSS_SELECTOR, ".news-entry__speech p")
    PRODUCT_BOX = (By.CSS_SELECTOR, ".catalog-offers .catalog-offers__container")
    PIZZA = (By.CSS_SELECTOR, '[data-item-id="domivetcinaigrq9"]')
    IMG_PIZZA = (By.CSS_SELECTOR, ".offers-description__image")
    NAME_PIZZA = (By.CSS_SELECTOR, '[class="catalog-masthead__title"]')
    TEXT_PIZZA = (By.CSS_SELECTOR, '[class="product-specs__main js-specs-main"]')

class SeazonvarLocators():
    BOX = (By.CSS_SELECTOR, '[class="headblock-search-txt"]')
    BUTTON = (By.XPATH, '//button[@class="btn head-btn"]')
    RESULTS_SEARCH = (By.CSS_SELECTOR, '.pgs-search-title')
    BUTTON_LOGIN_IN_SAIT = (By.CSS_SELECTOR, '[href="/?mod=login"]')
    BLOCK_LOGIN = (By.CSS_SELECTOR, '[class="content-wrap minheight"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[href="/?mod=reg"]')
    BLOCK_REGISTRATION = (By.CSS_SELECTOR, '[class="content-wrap minheight"]')

class StoreLokators():
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".login")
    INPUT_EMAIL = (By.CSS_SELECTOR, '#email_create')
    BUTTON_CREATE = (By.CSS_SELECTOR, '#SubmitCreate')

    NAME = (By.CSS_SELECTOR, '#customer_firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#customer_lastname')
    PASSWORD = (By.CSS_SELECTOR, '#passwd')
    ADRESS = (By.CSS_SELECTOR, '#address1')
    CITY = (By.CSS_SELECTOR, '#city')
    SHTAT = (By.CSS_SELECTOR, '#id_state')
    VALUE = (By.CSS_SELECTOR, 'value="1"')
    POST = (By.CSS_SELECTOR, '.form-control.uniform-input.text')
    PHONE = (By.CSS_SELECTOR, '#phone_mobile')
    NICNAME = (By.CSS_SELECTOR, '#alias')
    REG = (By.CSS_SELECTOR, '#submitAccount')
    WELCOME = (By.CSS_SELECTOR, '.info-account')
    EMAIL = (By.CSS_SELECTOR, '#email')
    PASSW = (By.CSS_SELECTOR, '#passwd')
    L_BUTTON = (By.CSS_SELECTOR, '#SubmitLogin')
    DRESS = (By.XPATH, '//ul[@class="sf-menu clearfix menu-content sf-js-enabled sf-arrows"]/li[2]/a')
    MODEL = (By.CSS_SELECTOR, '[class="ajax_block_product col-xs-12 col-sm-6 col-md-4 last-item-of-tablet-line"]')
    ADD = (By.CSS_SELECTOR, '[href="http://automationpractice.com/index.php?controller=cart&add=1&id_product=4&token=a47889c863e19a33d7d4eb4b46d5d0b5"]')
    CLOUSE_WINDOW = (By.CSS_SELECTOR, '.cross')
    CART = (By.CSS_SELECTOR, '[class="shopping_cart"] [href="http://automationpractice.com/index.php?controller=order"]')
    PRICE = (By.CSS_SELECTOR, '#product_price_4_16_472461')
    EXIT = (By.CSS_SELECTOR, '.logout')
    DELITE = (By.CSS_SELECTOR, '[href="http://automationpractice.com/index.php?controller=cart&delete=1&id_product=4&ipa=16&id_address_delivery=472461&token=a47889c863e19a33d7d4eb4b46d5d0b5"]')
    MESSAGE = (By.XPATH, '//p[text()="Your shopping cart is empty."]')






