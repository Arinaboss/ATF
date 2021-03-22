from Pages.lokators import NewsLokators

class News():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        browser.get(url)

    def news_box(self, browser):
        box = browser.find_element(*NewsLokators.NEWS_BOX)
        assert box.is_displayed() == True, f"expect {'news box'} got {'none'}"

    def image_in_box(self, browser):
        image_news = browser.find_element(*NewsLokators.IMAGE_IN_BOX)
        assert image_news.is_displayed() == True, f"expect {'news images'} got {'none'}"

    def name_box_news(self, browser):
        name_box = browser.find_element(*NewsLokators.NAME_BOX)
        assert name_box.is_displayed() == True, f"expect {'name box'} got {'none'}"

    def open_news(self, browser):
        link = browser.find_element(*NewsLokators.NAME_BOX)
        link.click()

    def news_image(self, browser):
        image = browser.find_element(*NewsLokators.IMAGE_NEWS)
        assert image.is_displayed() == True, f"expect {'image news'} got {'none'}"

    def name_news(self, browser):
        name = browser.find_element(*NewsLokators.NEWS_NAME)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", name)
        assert name.is_displayed() == True, f"expect {'name news'} got {'none'}"

    def text_news(self, browser):
        text = browser.find_element(*NewsLokators.TEXT_NEWS)
        browser.execute_script("return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);", text)
        assert text.is_displayed() == True, f"expect {'text news'} got {'none'}"
