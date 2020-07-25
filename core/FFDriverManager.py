from core.webDriverManager import MyWebDriverManager
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import DesiredCapabilities

class MyFirefoxDriverManager(MyWebDriverManager):

    def __init__(self):
        super().__init__()

    def createWebDriver(self):
        profile = webdriver.FirefoxProfile ()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(executable_path="C:\\MyWorkspace\\SeleniumFirefoxDriver\\2.6\\geckodriver.exe", firefox_profile=profile)
        driver.maximize_window()
        return driver
