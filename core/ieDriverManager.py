
from selenium import webdriver

from core.webDriverManager import MyWebDriverManager


class MyIeDriverManager(MyWebDriverManager):

    def __init__(self):
        super().__init__()

    def createWebDriver(self):
        capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
        #capabilities['acceptSslCerts'] = True
        driver = webdriver.Ie(executable_path="C:\\MyWorkspace\\IEDriver\\IEDriverServer.exe", capabilities=capabilities)
        driver.maximize_window()
        return driver
