from time import sleep

from pages.basePage import BasePage
from utils.logger import MyLogger
import logging
import random

class GuineenewsMenu(BasePage):

    mylg=MyLogger()
    logger = mylg.customLogger(logging.DEBUG)

    menu_acceuil = "//ul[@id='menu-mainmenu-1']/li[1]/a"
    menu_news = "//ul[@id='menu-mainmenu-1']/li[2]/a"
    menu_grands_dossiers = "//ul[@id='menu-mainmenu-1']/li[3]/a"
    menu_interviews = "//ul[@id='menu-mainmenu-1']/li[4]/a"
    menu_publireportage = "//ul[@id='menu-mainmenu-1']/li[5]/a"
    menu_region = "//ul[@id='menu-mainmenu-1']/li[6]/a"
    menu_sport = "//ul[@id='menu-mainmenu-1']/li[7]/a"
    menu_le_monde = "//ul[@id='menu-mainmenu-1']/li[8]/a"

    sub_menus_news = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a"
    sub_menus_grandossiers="//ul[@id='menu-mainmenu-1']/li[3]/ul[@class='sub-menu']//h3[@class='entry-title td-module-title']"
    sub_menus_publireportage = "//ul[@id='menu-mainmenu-1']/li[5]/ul//child::div[@class='block-mega-child-cats']/a"
    sub_menus_region = sub_menus_news = "//ul[@id='menu-mainmenu-1']/li[6]/ul//child::div[@class='block-mega-child-cats']/a"

    sub_menu_tous = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[1]"
    sub_menu_art_et_culture = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[2]"
    sub_menu_economie = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[3]"
    sub_menu_faits_divers = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[4]"
    sub_menu_politique = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[5]"
    sub_menu_revue_de_presse = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[6]"
    sub_menu_societe = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[7]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_rubrique(self, rubrique, locatorType="xpath"):
        if rubrique == "Acceuil":
            self.clickElement ( self.menu_acceuil, "xpath" )
            # self.waitForElementToBeClickable(self.menu, "id")

        if rubrique == "News":
            self.clickElement ( self.menu_news, "xpath" )

        if rubrique == "Grands_Dossiers":
            self.clickElement ( self.menu_grands_dossiers, "xpath" )

        if rubrique == "Interviews":
            self.clickElement ( self.menu_interviews, "xpath" )

        if rubrique == "Publireportage":
            self.clickElement ( self.menu_publireportage, "xpath" )

        if rubrique == "Region":
            self.clickElement ( self.menu_region, "xpath" )

        if rubrique == "Sport":
            self.clickElement ( self.menu_sport, "xpath" )

        if rubrique == "Le_monde":
            self.clickElement ( self.menu_le_monde, "xpath" )

    def move_mouse_on_main_menu_element(self, menu_locator, locatorType="xpath"):

        if menu_locator == "News":
            self.moveMouseOnElement(self.menu_news,locatorType)

        if menu_locator == "Grand_Dossiers":
            self.moveMouseOnElement(self.menu_grands_dossiers,locatorType)

        if menu_locator == "Publireportage":
            self.moveMouseOnElement(self.menu_publireportage,locatorType)

        if menu_locator == "Region":
            self.moveMouseOnElement(self.menu_region,locatorType)

    def go_to_news_sub_rubrique(self, sub_rubrique, locatorType="xpath"):

        if sub_rubrique == "Tous":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_tous, "xpath" )
            # self.waitForElementToBeClickable(self.menu, "id")

        if sub_rubrique == "art_et_culture":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_art_et_culture, "xpath" )

        if sub_rubrique == "Economie":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_economie, "xpath" )

        if sub_rubrique == "Faits_Divers":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_faits_divers, "xpath" )

        if sub_rubrique == "Politique":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_politique, "xpath" )

        if sub_rubrique == "Societe":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_societe, "xpath" )

        if sub_rubrique == "Revue_de_presse":
            self.move_mouse_on_main_menu_element(self.menu_news)
            self.clickElement ( self.sub_menu_revue_de_presse, "xpath" )

        if sub_rubrique == "Le_monde":
            self.clickElement ( self.menu_le_monde, "xpath" )

    def click_random_sub_article_in(self, menu, locatorType="xpath"):

        if menu == "Region":
            sub_menus = self.sub_menus_region
            main_menu = self.menu_region
        if menu == "Publi_reportage":
            sub_menus = self.sub_menus_publireportage
            main_menu = self.menu_publireportage
        if menu == "Grands_dossiers":
            sub_menus = self.sub_menus_grandossiers
            main_menu = self.menu_grands_dossiers

        self.move_mouse_on_main_menu_element (menu)
        sleep(2)
        #if menu == "menu_grands_dossiers":
        articles = self.getElements(sub_menus, "xpath")
        if len(articles) > 0:
            random_index = random.randint(1, len(articles))
            self.clickListElement(sub_menus,locatorType,random_index)

    def move_mouse_on(self, menu_locator, locatorType="xpath"):
        if menu_locator == "News":
            self.moveMouseOnElement(self.menu_news,locatorType)

        if menu_locator == "Politique":
            self.moveMouseOnElement(self.sub_menu_politique,locatorType)

        if menu_locator == "Revue":
            self.moveMouseOnElement(self.sub_menu_revue_de_presse,locatorType)

        if menu_locator == "Societe":
            self.moveMouseOnElement(self.sub_menu_societe,locatorType)
