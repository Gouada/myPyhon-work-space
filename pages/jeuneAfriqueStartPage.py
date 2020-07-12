from pages.basePage import BasePage
from utils.logger import MyLogger
import logging

class JeuneAfriqueStartPage(BasePage):

    iframe          = "//iframe[@name='__cmpLocator']"
    cookies_div     =   "//div[@id='main']"
    btn_accepter_cookies = "//button[@id='scmp-btn-allow']"  #"scmp-btn-allow"
    menu =  "main-menu-nav"
    btn_voir_tous_les_articles = "//div[@id='container__ribbon-cta']"
    btn_les_pays    = "//a[@class='header-nav-left open-country-selection']"
    btn_politique   = "//nav['main-navigation']//a[contains(@data-label, 'Politique')]"
    #btn_politique   = "//a[contains(@data-label, 'Politique')]" #"//a[contains(@data-label, 'dropdown-menu Politique')]" #"//a[contains(@href,'/rubriques/politique/')]"
    btn_economie    = "//a[contains(@data-label, 'Économie')]"
    btn_societe     = "//a[contains(@data-label, 'Société')]" #"//a[contains(@data-category,'menu-main-navigation Menu Principal par défaut') and contains(@href,'/rubriques/societe/')]"
    btn_culture     = "//a[contains(@data-label, 'Culture')]" #"//a[contains(@data-category,'menu-main-navigation Menu Principal par défaut') and contains(@href,'/rubriques/culture/')]"
    btn_sport       = "//a[contains(@data-label, 'Sport')]" #"//a[contains(@data-category,'menu-main-navigation Menu Principal par défaut') and contains(@href,'/rubriques/sport/')]"
    btn_lifestyle   = "//a[contains(@data-label, 'Lifestyle')]" #"//a[contains(@data-category,'menu-main-navigation Menu Principal par défaut') and contains(@href,'/campagnes-luxe/')]"

    myLg = MyLogger()
    logger = myLg.customLogger ( logging.DEBUG )

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        try:
            print("current_handle............")
            print(self.driver.current_window_handle)
            handles = self.driver.window_handles
            #iframe = self.getElement(self.iframe, "xpath")
            #self.driver.switch_to.frame(self.iframe)
            #self.driver.switch_to.active_element ()
            #self.waitForElementToBeClickable(self.btn_accepter_cookies,"id", 10, 1)
            #if self.isClickable(self.btn_accepter_cookies,"xpath"):
            self.clickElement(self.btn_accepter_cookies,"xpath")
            #self.clickElement(self.btn_voir_tous_les_articles,"xpath")
            #self.driver.switch_to.default_content ()
        except Exception as error:
            self.logger.error(error)

    def go_to_rubrique(self, rubrique, locatorType="xpath"):
        if rubrique == "Politique":
            self.clickElement(self.btn_politique, "xpath")
            #self.waitForElementToBeClickable(self.menu, "id")

        if rubrique == "Economie":
            self.clickElement(self.btn_economie, "xpath")

        if rubrique == "Societe":
            self.clickElement(self.btn_societe, "xpath")

        if rubrique == "Culture":
            self.clickElement(self.btn_culture, "xpath")

        if rubrique == "Lifestyle":
            self.clickElement(self.btn_lifestyle, "xpath")

        if rubrique == "Sport":
            self.clickElement(self.btn_sport, "xpath")