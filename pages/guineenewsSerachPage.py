
from pages.basePage import BasePage

class GuineenewsSearchPage(BasePage):

    pages = "//span[contains(@class, 'pages') and contains(text(), 'Page * sur') ]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_more_than_one_result_page(self):
        if self.getElement(self.pages, "xpath") is not None:
            return True
        else:
            return False

