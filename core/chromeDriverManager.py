from selenium import webdriver

from core.webDriverManager import MyWebDriverManager


class MyChromeDriverManager(MyWebDriverManager):

    driver = None
    def __init__(self):
        super().__init__()

    def createWebDriver(self):
        print("creating chrome driver....")
        options = webdriver.ChromeOptions ()
        options.add_argument ( '--ignore-certificate-errors' )
        options.add_argument ( '--ignore-certificate-errors-spki-list' )
        options.add_argument ( '--ignore-ssl-errors' )
        self.driver = webdriver.Chrome( executable_path="C:\\MyWorkspace\\SeleniumChromeDriver\\85\\chromedriver.exe", options=options)
        self.driver.maximize_window()
        return self.driver

    def getUrl(self, url):
        self.driver.get(url)