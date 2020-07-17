import unittest
from time import sleep

import pytest

from pages.guineenewsMenu import GuineenewsMenu
from pages.guineenewsStartPage import GuineenewsStartPage
from utils.logger import MyLogger
import logging
from core.driverFactory import MyDriverFactory
from constants.pages import Pages
from ddt import ddt, data, unpack, file_data
from utils.csvFileReader import readCSV


@ddt
class GuineenewsStartPageTest ( unittest.TestCase ):
    lg = MyLogger ()
    logger = lg.customLogger ( logging.DEBUG )

    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.driver = MyDriverFactory.getDriverManager ( "CHROME" ).getDriver ()
            cls.logger.info ( "driver was successfuly created" )
            cls.startPage = GuineenewsStartPage ( cls.driver )
            cls.menuPage = GuineenewsMenu ( cls.driver )
        except Exception as error:
            cls.logger.error ( error )

    def setUp(self) -> None:
        pass

    @pytest.mark.run ( order=1 )
    def test_start_guineenews(self):
        try:
            self.driver.get ( Pages.getPageURL ( "guineenewsStartPage" ) )
            self.logger.info ( "Guineenews started successfully" )
            # current_hd = self.driver.current_window_handle
            # self.logger.info("current handle"+current_hd)
            # hd = self.driver.window_handles
            # if hd is not None:
            #     for h in hd:
            #         self.logger.info(h)
            # self.startPage.takescreenShotOnError("test_start_guineenews")
            self.driver.switch_to.default_content ()
            # sleep(5)
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=2 )
    def test_click_sport(self):
        sleep ( 10 )
        # self.startPage.takescreenShotOnError("before_clicking_sport")
        self.startPage.go_to_rubrique ( "Sport" )
        # self.startPage.takescreenShotOnError("after_clicking_sport")

    @pytest.mark.run ( order=3 )
    def test_Mouse_0n_News(self):
        try:
            self.menuPage.move_mouse_on ( "News" )
            sleep ( 2 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=4 )
    def test_Mouse_0n_Politique(self):

        try:
            self.menuPage.move_mouse_on ( "Politique" )
            sleep ( 2 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=5 )
    def test_Mouse_0n_Revue_de_Presse(self):

        try:
            self.menuPage.move_mouse_on ( "Revue" )
            sleep ( 2 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=6 )
    def test_Mouse_0n_Societe(self):

        try:
            self.menuPage.move_mouse_on ( "Societe" )
            sleep ( 2 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=7 )
    def test_click_Random_article_in_Revue_de_Presse(self):

        try:
            self.menuPage.click_random_sub_article_in ( "Region" )
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=8 )
    #@data ("Alpha code", "Cellou Dalein Diallo")
    @file_data("C:\\MyWorkspace\\python_workspace\\myFrameWork\\testData.json")
    @unpack
    def test_search_text_alpha_conde(self, txt):
        try:
            self.startPage.search ( txt )
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=9 )
    # @data ("Alpha code", "Cellou Dalein Diallo")
    @data ( *readCSV("C:\\MyWorkspace\\python_workspace\\myFrameWork\\resources\\testData.csv" ))
    @unpack
    def test_search_text_Titi(self, txt):
        try:
            self.startPage.search ( txt )
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver is not None:
            #cls.driver.implicitly_wait (5)
            sleep ( 5 )
            cls.driver.close ()
            # cls.driver.quit
