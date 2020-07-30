import logging

from behave import fixture, use_fixture

from constants.browser import Browsers
from core.driverFactory import MyDriverFactory
from utils.logger import MyLogger


# import unittest

@fixture
def setUpClass(context):
    driver = MyDriverFactory.getDriverManager ( Browsers.chrome ).getDriver()
    context.driver = driver
    lg = MyLogger ()
    context.logger = lg.customLogger ( logging.DEBUG )
    yield context.driver
    if context.driver is not None:
        context.driver.close ()

def before_all(context):
    use_fixture(setUpClass, context)
