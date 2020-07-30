
import unittest
from time import sleep

import pytest
from behave import *  # given, when, then
from pytest import fail

from constants.guineenewsMenu_cats import Menu
from constants.urls import Urls
from pages.guineenewsMenu import GuineenewsMenu
from pages.guineenewsSerachPage import GuineenewsSearchPage
from pages.guineenewsStartPage import GuineenewsStartPage


@pytest.mark.usefixtures
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
            context.searchPage = GuineenewsSearchPage ( context.driver )
            sleep(2)
            context.startPage.scrollUpToTop()
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error(error)
            context.startPage.takescreenShotOnError("i start_the_site_guineenews")

    @when ('I click on politique')
    def step_impl(context):
        #try:
            context.menuPage.go_to_sub_menu( Menu.News, Menu.Politique )
            sleep ( 5 )
        # except Exception as error:
        #     fail ( 'Step fail with {}'.format ( str ( error ) ) )
        #     context.logger.error ( error )
        #     context.startPage.takescreenShotOnError("i_click_on_politique")

    @then('I click on Societe')
    def step_impl(context):
        try:
            #sleep ( 3 )
            context.menuPage.go_to_sub_menu (Menu.News, Menu.Societe )
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
