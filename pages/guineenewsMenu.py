from time import sleep

from pages.basePage import BasePage
from utils.logger import MyLogger
import logging
import random
from constants.guineenewsMenu_cats import Menu

class GuineenewsMenu(BasePage):

    mylg=MyLogger()
    logger = mylg.customLogger(logging.DEBUG)

    logo = "//div[@class='td-main-menu-logo td-logo-in-header td-logo-sticky']/a[@class='td-main-logo']"

    menu_acceuil = "//ul[@id='menu-mainmenu-1']/li[1]/a"
    menu_news = "//ul[@id='menu-mainmenu-1']/li[2]/a"
    menu_grands_dossiers = "//ul[@id='menu-mainmenu-1']/li[3]/a"
    menu_interviews      = "//ul[@id='menu-mainmenu-1']/li[4]/a"
    menu_publireportage = "//ul[@id='menu-mainmenu-1']/li[5]/a"
    menu_region = "//ul[@id='menu-mainmenu-1']/li[6]/a"
    menu_sport = "//ul[@id='menu-mainmenu-1']/li[7]/a"
    menu_le_monde = "//ul[@id='menu-mainmenu-1']/li[8]/a"

    sub_menus_news = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a"
    sub_menus_grandossiers  = "//ul[@id='menu-mainmenu-1']/li[3]/ul//child::h3[@class='entry-title td-module-title']/a"
    sub_menus_publireportage = "//ul[@id='menu-mainmenu-1']/li[5]/ul//child::h3[@class='entry-title td-module-title']/a"
    sub_menus_region         = "//ul[@id='menu-mainmenu-1']/li[6]/ul//child::div[@class='block-mega-child-cats']/a"

    sub_menu_tous = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[1]"
    sub_menu_art_et_culture = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[2]"
    sub_menu_faits_divers = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[4]"
    sub_menu_economie = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[3]"
    sub_menu_politique ="//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[5]"
    sub_menu_revue_de_presse = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[6]"
    sub_menu_societe = "//ul[@id='menu-mainmenu-1']/li[2]/ul//child::div[@class='block-mega-child-cats']/a[7]"

    search_icon = 'td-header-search-button' #"//a[@id='td-header-search-button']"
    search_field = 'td-header-search' #"//input[@id='td-header-search']"
    search_btn = 'td-header-search-top' #"//input[@id='td-header-search-top']"

    articles_filter = "//div[contains(@class,'td-subcat-more') and contains(text(), 'Dernier')]"
    filter_ul = "//div[@class='td-pulldown-filter-display-option']//child::ul[@class='td-pulldown-filter-list']"
    filter_lis = "//div[@class='td-pulldown-filter-display-option']//child::li[@class='td-pulldown-filter-item']"

    filter_result_list = "//div[@class='td-ss-main-content']//h3/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

    def move_mouse_on_main_menu_element(self, menu_locator, locatorType="xpath"):

        if menu_locator == Menu.News:
            self.moveMouseOnElement(self.menu_news,locatorType)

        if menu_locator == Menu.Grands_Dossiers:
            self.moveMouseOnElement(self.menu_grands_dossiers,locatorType)

        if menu_locator == Menu.Publireportage:
            self.moveMouseOnElement(self.menu_publireportage,locatorType)

        if menu_locator == Menu.Region:
            self.moveMouseOnElement(self.menu_region,locatorType)
        #sleep(2)

    def go_to_news_sub_rubrique(self, sub_rubrique, locatorType="xpath"):

        self.move_mouse_on ( Menu.News, locatorType )
        sleep(3)
        if sub_rubrique == Menu.Tous:
            element = self.waitForElementToBe(self.sub_menu_tous)
            self.clickElement(element=element)
            # self.waitForElementToBe(self.menu, "id")

        if sub_rubrique == Menu.Art_et_Culture:
            element = self.waitForElementToBe (self.sub_menu_art_et_culture)
            self.clickElement(element=element)

        if sub_rubrique == Menu.Economie:
            element = self.waitForElementToBe (self.sub_menu_economie, locatorType=locatorType, event="visible")
            self.clickElement ( element=element )
            #self.clickElement ( self.sub_menu_economie, locatorType )

        if sub_rubrique == Menu.Faits_Divers:
            element = self.waitForElementToBe (self.sub_menu_faits_divers)
            self.clickElement (element=element)

        if sub_rubrique == Menu.Politique:
            element = self.waitForElementToBe ( self.sub_menu_politique )
            self.clickElement ( element=element )

        if sub_rubrique == Menu.Societe:
            element = self.waitForElementToBe ( self.sub_menu_societe,locatorType="xpath", event="visible" )
            self.clickElement ( element=element )

        if sub_rubrique == Menu.Revue_de_presse:
            element = self.waitForElementToBe ( self.sub_menu_revue_de_presse )
            self.clickElement ( element=element )

        #if sub_rubrique == "Le_monde":
         #   self.clickElement ( self.menu_le_monde, "xpath" )

    def click_random_sub_article_in(self, menu, locatorType="xpath"):

        if menu == Menu.Region:
            sub_menus = self.sub_menus_region
            main_menu = self.menu_region
        if menu == Menu.Publireportage:
            sub_menus = self.sub_menus_publireportage
            main_menu = self.menu_publireportage
        if menu == Menu.Grands_Dossiers:
            #self.logger.warning(self.sub_menus_grandossiers)
            sub_menus = self.sub_menus_grandossiers
            main_menu = self.menu_grands_dossiers

        self.move_mouse_on_main_menu_element (menu)
        #sleep(2)
        #if menu == "menu_grands_dossiers":
        articles = self.getElements(sub_menus, "xpath")
        if len(articles) > 0:
            random_index = random.randint(1, len(articles))
            self.clickListElement(sub_menus,locatorType,random_index)

    def move_mouse_on(self, menu_locator, locatorType="xpath"):
        if menu_locator == Menu.News:
            self.moveMouseOnElement(self.menu_news,locatorType)

        if menu_locator == Menu.Politique:
            self.moveMouseOnElement(self.sub_menu_politique,locatorType)

        if menu_locator == Menu.Revue_de_presse:
            self.moveMouseOnElement(self.sub_menu_revue_de_presse,locatorType)

        if menu_locator == Menu.Societe:
            self.moveMouseOnElement(self.sub_menu_societe,locatorType)

    def search(self, txt):
        self.clickElement(self.search_icon)
        searchField_input = self.waitForElementToBe( self.search_field, "id", event="visible" )
        self.clearField(element=searchField_input)
        self.typeTextInField(text=txt, element=searchField_input)
        self.clickElement(self.search_btn, "id")

    def select_from_derniers_drop_down_Menu(self, criteria):

        self.moveMouseOnElement(self.articles_filter, "xpath")
        filter_elements = self.waitForElementToBe(self.filter_lis, locatorType="xpath",event="clickable")

        if(criteria == Menu.Filter_cretaria_vedette):
            self.clickListElement(elementPosition=1, element=filter_elements)

        if (criteria == Menu.Filter_cretaria_plus_populaire):
            self.clickListElement ( elementPosition=2, element=filter_elements )

        if (criteria == Menu.Filter_cretaria_7_j_populaire):
            self.clickListElement ( elementPosition=3, element=filter_elements )

        if (criteria == Menu.Filter_cretaria_mieux_notes):
            self.clickListElement ( elementPosition=4, element=filter_elements )

        if (criteria == Menu.Filter_cretaria_hasard):
            self.clickListElement ( elementPosition=5, element=filter_elements )

    def click_logo(self):
        self.clickElement(myLocator=self.logo,locatorType="xpath")