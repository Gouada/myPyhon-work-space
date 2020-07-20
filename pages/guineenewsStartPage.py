from constants.guineenewsMenu_cats import Menu
from pages.basePage import BasePage
from utils.logger import MyLogger
import logging

class GuineenewsStartPage(BasePage):
    lg = MyLogger ()
    logger = lg.customLogger ( logging.DEBUG )

    menu_acceuil="//ul[@id='menu-mainmenu-1']/li[1]/a"
    menu_news="//ul[@id='menu-mainmenu-1']/li[2]/a"
    menu_grands_dossiers = "//ul[@id='menu-mainmenu-1']/li[3]/a"
    menu_interviews = "//ul[@id='menu-mainmenu-1']/li[4]/a"
    menu_publireportage = "//ul[@id='menu-mainmenu-1']/li[5]/a"
    menu_region = "//ul[@id='menu-mainmenu-1']/li[6]/a"
    menu_sport = "//ul[@id='menu-mainmenu-1']/li[7]/a"
    menu_le_monde = "//ul[@id='menu-mainmenu-1']/li[8]/a"

    sub_menu_tous = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[1]"
    sub_menu_art_et_culture = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[2]"
    sub_menu_economie = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[3]"
    sub_menu_faits_divers = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[4]"
    sub_menu_politique = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[5]"
    sub_menu_revue_de_presse = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[6]"
    sub_menu_societe = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[7]"

    search_icon = 'td-header-search-button' #"//a[@id='td-header-search-button']"
    search_field = 'td-header-search' #"//input[@id='td-header-search']"
    search_btn = 'td-header-search-top' #"//input[@id='td-header-search-top']"

    def __init__(self, driver):
        try:
            super().__init__(driver)
            self.driver = driver
            self.logger.info("StartPage successfully created")
        except Exception as error:
            self.logger.error(error)

    def go_to_rubrique(self, rubrique, locatorType="xpath"):
        if rubrique == Menu.Acceuil:
            self.clickElement ( self.menu_acceuil, "xpath" )
            # self.waitForElementToBe(self.menu, "id")

        if rubrique == Menu.News:
            self.clickElement ( self.menu_news, "xpath" )

        if rubrique == Menu.Grands_Dossiers:
            self.clickElement ( self.menu_grands_dossiers, "xpath" )

        if rubrique == Menu.Interviews:
            self.clickElement ( self.menu_interviews, "xpath" )

        if rubrique == Menu.Publireportage:
            self.clickElement ( self.menu_publireportage, "xpath" )

        if rubrique == Menu.Region:
            self.clickElement ( self.menu_region, "xpath" )

        if rubrique == Menu.Sport:
            self.clickElement ( self.menu_sport, "xpath" )

        if rubrique == Menu.Le_Monde:
            self.clickElement ( self.menu_le_monde, "xpath" )

    def go_to_sub_rubrique(self, sub_rubrique, locatorType="xpath"):

        if sub_rubrique == Menu.Tous:
            self.clickElement ( self.sub_menu_tous, "xpath" )
            # self.waitForElementToBe(self.menu, "id")

        if sub_rubrique == Menu.Art_et_Culture:
            self.clickElement ( self.sub_menu_art_et_culture, "xpath" )

        if sub_rubrique == Menu.Economie:
            self.clickElement ( self.sub_menu_economie, "xpath" )

        if sub_rubrique == Menu.Faits_Divers:
            self.clickElement ( self.sub_menu_faits_divers, "xpath" )

        if sub_rubrique == Menu.Politique:
            self.clickElement ( self.sub_menu_politique, "xpath" )

        if sub_rubrique == Menu.Societe:
            self.clickElement ( self.sub_menu_societe, "xpath" )

        if sub_rubrique == Menu.Revue_de_presse:
            self.clickElement ( self.sub_menu_revue_de_presse, "xpath" )

        if sub_rubrique == Menu.Le_Monde:
            self.clickElement ( self.menu_le_monde, "xpath" )

    def move_mouse_on(self, menu_locator, locatorType="xpath"):
        if menu_locator == Menu.News:
            self.moveMouseOnElement(self.menu_news,locatorType)

        if menu_locator == Menu.Politique:
            self.moveMouseOnElement(self.sub_menu_politique,locatorType)

        if menu_locator == Menu.Revue_de_presse:
            self.moveMouseOnElement(self.sub_menu_revue_de_presse,locatorType)

    def search(self, txt):
        self.clickElement(self.search_icon)
        searchField_input = self.waitForElementToBe( self.search_field, "id", event="visible" )
        self.clearField(element=searchField_input)
        self.typeTextInField(text=txt, element=searchField_input)
        self.clickElement(self.search_btn, "id")
