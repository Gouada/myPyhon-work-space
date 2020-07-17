import logging
from time import sleep

from behave import fixture, use_fixture
#import unittest

from core.driverFactory import MyDriverFactory
from utils.logger import MyLogger


@fixture
def setUpClass(context):
    driver = MyDriverFactory.getDriverManager ( "CHROME" ).getDriver()
    context.driver = driver
    lg = MyLogger ()
    context.logger = lg.customLogger ( logging.DEBUG )
    yield context.driver
    if context.driver is not None:
        #context.driver.implicitly_wait ( 5 )
        sleep ( 5 )
        context.driver.close ()

def before_all(context):
    use_fixture(setUpClass, context)
