
from core.seleniumDriverWrapper import SeleniumDriverWrapper
from constants.pages import Pages
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium.common.exceptions import *

class BasePage(SeleniumDriverWrapper):

    rubrik = "//h1[@class='entry-title td-page-title']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getPageTitle__(self):
        return self.getPageTitle()

    def waitPageToLoad(self, page):

        wait = WebDriverWait(self.driver,timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                                           ElementNotSelectableException,
                                                                                           NoSuchElementException])
        elt = wait.until(e_c.title_is(page.title))

    def rubrikTitle(self):
        return self.getElementText(self.rubrik, "xpath")
        #self.getPageTitle()