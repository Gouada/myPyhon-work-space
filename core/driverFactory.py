
from selenium import webdriver

from core.FFDriverManager import MyFirefoxDriverManager
from core.chromeDriverManager import MyChromeDriverManager
from core.ieDriverManager import MyIeDriverManager


class MyDriverFactory():

    def __init__(self, browser):
        pass

    @staticmethod
    def getDriverManager(browser="CHROME"):

        driverManager = None
        if browser.upper() == "CHROME":
            driverManager = MyChromeDriverManager()
        if browser.upper() == "FIREFOX":
            driverManager = MyFirefoxDriverManager()
        if browser.upper() == "IE":
            driverManager = MyIeDriverManager()
        #else:
         #   driverManager = MyChromeDriverManager()
        return driverManager
