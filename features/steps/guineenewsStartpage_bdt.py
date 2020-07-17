
import unittest
from time import sleep

from utils.logger import MyLogger
from behave import * #given, when, then
from constants.pages import Pages
from core.driverFactory import MyDriverFactory
from pages.guineenewsStartPage import GuineenewsStartPage
from pages.guineenewsMenu import GuineenewsMenu
from pages.guineenewsStartPage import GuineenewsStartPage
import logging

class GuineenewsStratPage(unittest.TestCase):


    #context.logger = logger
    #driver = None

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.driver = MyDriverFactory.getDriverManager( "CHROME" ).getDriver()
    # @fixture()
    # def getMenuPage(self):
    #     self.menuPage = GuineenewsMenu ( self.driver )
    #     lg = MyLogger ()
    #     self.logger = lg.customLogger ( logging.DEBUG )

    #def before_step(self):
       # use_fixture( self.getMenuPage )

    @given ('i start the site guineenews')
    def step_impl(context):
        try:
            context.driver.get(Pages.getPageURL ( "guineenewsStartPage" ))
            context.startPage = GuineenewsStartPage ( context.driver )
        except Exception as error:
            context.logger.error(error)

    @when ('i click on politique')
    def step_impl(context):
        try:
            #menuPage = GuineenewsMenu ( context.driver )
            #startPage = GuineenewsStartPage(context.driver)
            context.startPage.go_to_rubrique ( "Sport" )
            context.logger.info("whatsapp")
            #menuPage.move_mouse_on ( "Politique" )
            sleep ( 3 )
        except Exception as error:
            context.logger.error ( error )

    @then('i click on societe')
    def step_impl(context):
        try:
            #context.menuPage = GuineenewsMenu ( context.driver )
            #context.startPage = GuineenewsStartPage ( context.driver)
            context.startPage.go_to_rubrique ("Le_monde")
        except Exception as error:
            context.logger.error(error)