
from core.seleniumDriverWrapper import SeleniumDriverWrapper
from constants.pages import Pages
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium.common.exceptions import *

class BasePage(SeleniumDriverWrapper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getPageTitle(self):
        return self.driver.title

    def waitPageToLoad(self, page):

        wait = WebDriverWait(self.driver,timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                                           ElementNotSelectableException,
                                                                                           NoSuchElementException])
        elt = wait.until(e_c.title_is(page.title))
