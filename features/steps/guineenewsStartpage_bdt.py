
import unittest
from time import sleep

from pytest import fail

from utils.logger import MyLogger
from behave import * #given, when, then
from constants.pages import Pages
from core.driverFactory import MyDriverFactory
from pages.guineenewsStartPage import GuineenewsStartPage
from pages.guineenewsMenu import GuineenewsMenu
from pages.guineenewsStartPage import GuineenewsStartPage
import logging
from constants.urls import Urls
from constants.guineenewsMenu_cats import Menu

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

    @given ('I start the site guineenews')
    def step_impl(context):
        try:
            #context.driver.get(Pages.getPageURL ( "guineenewsStartPage" ))
            context.driver.get(Urls.startPage_guineenews)
            context.startPage = GuineenewsStartPage ( context.driver )
            context.menuPage = GuineenewsMenu(context.driver)
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error(error)
            context.startPage.takescreenShotOnError("i start_the_site_guineenews")

    @when ('I click on politique')
    def step_impl(context):
        try:
            context.menuPage.go_to_news_sub_rubrique(Menu.Politique)
            sleep ( 3 )
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error ( error )
            context.startPage.takescreenShotOnError("i_click_on_politique")

    @then('I click on societe')
    def step_impl(context):
        try:
            context.menuPage.go_to_news_sub_rubrique (Menu.Societe)
            sleep ( 3 )
        except Exception as error:
            fail('Step fail with {}'.format(str(error)) )
            context.logger.error(error)
            context.startPage.takescreenShotOnError("i_click_on_societe")

    @then('I click a random Region')
    def step_impl(context):
        try:
            context.menuPage.click_random_sub_article_in( Menu.Region )
            sleep ( 3 )
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error(error)
            context.menuPage.takescreenShotOnError("I_click_a_random_region")

    @then ( 'I click a random grands dossiers' )
    def step_impl(context):
        try:
            context.menuPage.click_random_sub_article_in ( Menu.Grands_Dossiers )
            sleep ( 3 )
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error ( error )
            context.menuPage.takescreenShotOnError ( "I_click_a_random_grands_dossiers" )

    @then('I click a random publireportage')
    def step_impl(context):
        try:
            context.menuPage.click_random_sub_article_in( Menu.Publireportage )
            sleep ( 3 )
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error(error)
            context.menuPage.takescreenShotOnError("I_click_a_random_publireportage")