
from pages.basePage import BasePage

class GuineenewsSearchPage(BasePage):

    pages = "//span[contains(@class, 'pages') and contains(text(), 'Page * sur') ]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



