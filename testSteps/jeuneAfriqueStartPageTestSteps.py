from time import sleep

from constants.pages import Pages
from core import driverFactory
from constants.pages import Pages
import unittest

from pages.jeuneAfriqueStartPage import JeuneAfriqueStartPage
from utils.logger import MyLogger
import logging
import pytest
import pytest_ordering

#from constants.pages import Pages as pg
class JeuneAfriqueStartPageTestSteps(unittest.TestCase):
    driver = None
    myLg = MyLogger ()
    logger = myLg.customLogger(logging.DEBUG)

    @classmethod
    def setUpClass(cls) -> None:
        #cls.logger = cls.
        if driverFactory.MyDriverFactory.getDriverManager("CHROME") is not None:
            cls.driver = driverFactory.MyDriverFactory.getDriverManager("CHROME").getDriver()
            cls.startPage = JeuneAfriqueStartPage(cls.driver)
        else:
            cls.logger.error("drivermanager is null")

    def setUp(self) -> None:
        pass

    @pytest.mark.run ( order=1 )
    def test_startjeuneAfrique(self):
        if self.driver is not None:
            self.driver.get ( Pages.getPageURL ( "startPage" ) )
            self.startPage.accept_cookies ()
            # sleep (3)
        else:
            self.logger.error ( "driver is null" )

    @pytest.mark.run(order=2)
    def test_go_to_politique_page(self):
       try:
           #self.driver.implicitly_wait(15)
            self.startPage.go_to_rubrique( "Politique" )
            #self.driver.get ( Pages.getPageURL ( "politiquePage" ) )
            self.logger.info("... going to politique page ...")
            self.driver.implicitly_wait(3)
            #sleep (3)
       except Exception as error:
        self.logger.error(error)

    @pytest.mark.run(order=3)
    def test_go_to_culture_page(self):
        try:
            self.startPage.go_to_rubrique("Culture")
            self.logger.info("... going to culture page ...")
            sleep ( 3 )
        except Exception as error:
            self.logger.error(error)

    @pytest.mark.run ( order=4 )
    def test_scrolltoBottom(self):
        try:
            self.startPage.scrollDownToBottom ()
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=5 )
    def test_scrolltoTop(self):
        try:
            self.startPage.scrollUpToTop ()
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run(order=6)
    def test_go_to_societe_page(self):
        try:
            self.startPage.go_to_rubrique("Societe")
            self.logger.info("... going to societe page ...")
            sleep ( 3 )
        except Exception as error:
            self.logger.error(error)

    @pytest.mark.run ( order=7 )
    def test_go_to_sport_page(self):
        try:
            self.startPage.go_to_rubrique ( "Sport" )
            self.logger.info ( "... going to sport page ..." )
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run ( order=8 )
    def test_go_to_lifestyle_page(self):
        try:
            self.startPage.go_to_rubrique ( "Lifestyle" )
            self.logger.info ( "... going to lifestyle page ..." )
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    @pytest.mark.run (order=9)
    def test_go_to_economie_page(self):
        try:
            self.startPage.go_to_rubrique("Economie")
            self.logger.info ( "... going to economie page ..." )
            sleep ( 3 )
        except Exception as error:
            self.logger.error ( error )

    # @pytest.mark.run(order=7)
    # def test_go_back(self):
    #     try:
    #         self.startPage.goBack()
    #         self.logger.info("... going back ...")
    #         sleep(3)
    #     except Exception as error:
    #         self.logger.error(error)


    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.driver is not None:
            cls.driver.quit()