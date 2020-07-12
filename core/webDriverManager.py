from abc import abstractmethod
from selenium import webdriver

class MyWebDriverManager:

    driver = None
    def __init__(self):
        pass

    @abstractmethod
    def createWebDriver(self):
        pass

    def getDriver(self):
        if self.driver is None:
            self.driver = self.createWebDriver()
            print("returning driver")
        return self.driver

    def quitDriver(self, driver):
        if driver is not None:
            try:
                driver.quit()
            except Exception as ex:
                print("error occured")


    def closeDriver(self, driver):
        if driver is not None:
            try:
                driver.close()
            except Exception as ex:
                print("error closing browser")

