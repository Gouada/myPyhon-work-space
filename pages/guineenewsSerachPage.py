import math
import random
from time import sleep

from pages.basePage import BasePage

class GuineenewsSearchPage(BasePage):

    pages = "//span[contains(@class, 'pages') and contains(text(), 'Page') and contains(text(), 'sur') ]"
    next_page_icon = "//div['page-nav td-pb-padding-side']/child::a/i[@class='td-icon-menu-right']/parent::a"
    previous_page_icon = "//div['page-nav td-pb-padding-side']/child::a/i[@class='td-icon-menu-left']/parent::a"
    result_list = "//div[@class='td-ss-main-content']//child::h3[@class='entry-title td-module-title']/a"

    logo = "//div[@class='td-main-menu-logo td-logo-in-header td-logo-sticky']/a[@class='td-main-logo']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_more_than_one_result_page(self):
        if self.isVisible(self.pages, "xpath") is not None:
            return True
        else:
            return False

    def paginate_to_next_Page(self):
        element = self.getElement(self.next_page_icon, "xpath")
        self.scrollElementIntoView(element)
        sleep(2)
        self.clickElement(element=element)

    def click_a_random_search_result(self):

        elements = self.getElements(self.result_list, "xpath")
        if len(elements) > 0:
            random_index = random.randint(0, (len(elements)-1))
            element = self.getListElement(self.result_list, "xpath", random_index)
            self.scrollElementIntoView(element)
            sleep(4)
            self.clickElement(element=element)

    def click_a_specific_search_result(self, position):

        elements = self.getElements(self.result_list, "xpath")
        if len(elements) > 0:
            if position == "last":
                article_index = len(elements) -1
            else:
                article_index = position
            element = self.getListElement(self.result_list, "xpath", article_index)
            self.scrollElementIntoView(element)
            sleep(3)
            self.clickElement(element=element)