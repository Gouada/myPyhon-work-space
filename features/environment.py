import logging
from time import sleep

from behave import fixture, use_fixture
#import unittest

from core.driverFactory import MyDriverFactory
from utils.logger import MyLogger
from constants.browser import Browsers

@fixture
def setUpClass(context):
    driver = MyDriverFactory.getDriverManager ( Browsers.firefox ).getDriver()
    context.driver = driver
    lg = MyLogger ()
    context.logger = lg.customLogger ( logging.DEBUG )
    yield context.driver
    if context.driver is not None:
        context.driver.close ()

def before_all(context):
    use_fixture(setUpClass, context)
