from datetime import datetime

import now as now
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.actions import *
from selenium.common.exceptions import *
from utils.logger import MyLogger
import logging

import time

class SeleniumDriverWrapper:

    mylogger = MyLogger ()
    logger = mylogger.customLogger ( logging.DEBUG )

    logger = None
    def __init__(self, driver):
        self.driver = driver


    def getByType(self, locatorType):
        #webdriver.Chrome.m
        wb=None
        try:
            if locatorType.upper() == "ID":
              return By.ID
            if locatorType.upper() == "NAME":
              return By.NAME
            if locatorType.upper() == "CLASS_NAME":
              return By.CLASS_NAME
            if locatorType.upper() == "TAG_NAME":
              return By.TAG_NAME
            if locatorType.upper() == "LINK_TEXT":
              return By.LINK_TEXT
            if locatorType.upper() == "PARTIAL_LINK_TEXT":
              return By.PARTIAL_LINK_TEXT
            if locatorType.upper() == "XPATH":
              return By.XPATH
        except Exception as error:
            self.logger.error(error)

    def getElement(self, myLocator, locatorType="id"):
        """
        :type locator: string
        """
        byType=None
        try:
            byType = self.getByType(locatorType)
            self.logger.info(byType)
            self.logger.info(".....myLocator.................................................."+myLocator)
            el = self.driver.find_element(byType, myLocator)
            return el
        except (Exception, NoSuchElementException) as error:
            self.logger.error(error)

    def getElements(self, myLocator, locatorType="id"):
        """
        :type locator: string
        """
        try:
            by = self.getByType(locatorType)
            el = self.driver.find_elements(by, myLocator)
            return el
        except (Exception, NoSuchElementException) as error:
            self.logger.error(error)

    def clickElement(self, myLocator, locatorType="id"):
        try:
            self.getElement(myLocator, locatorType).click()
        except ElementNotVisibleException as error:
            self.logger(error)

    def typeTextInField(self, myLocator, locatorType,text):
        try:
            self.getElement(myLocator, locatorType).send_keys(text)
        except ElementNotVisibleException as error:
            self.logger(error)

    def clearField(self, myLocator, locatorType,text):
        try:
            self.getElement(myLocator, locatorType).clear()
        except ElementNotVisibleException as error:
            self.logger(error)

    def getElementText(self, myLocator, locatorType):
        self.getElement(myLocator, locatorType).text


    def getTagName(self, myLocator, locatorType):
        self.getElement(myLocator, locatorType).tag_name

    def isEnabled(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).is_enabled()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def isVisible(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).is_displayed()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def isSelected(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).is_selected()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    #def isEmpty(self, myLocator, locatorType):
     #   self.getElement(myLocator, locatorType).

    def isChecked(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).get_attribute("checked")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def isFocused(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).get_attribute("focused")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def isClickable(self, myLocator, locatorType):
        try:
            byType = self.getByType(locatorType)
            self.getElement(myLocator, byType).get_attribute("clickable")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def getClassName(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).get_attribute("classname")
            #webdriver.Chrome.find_elements(By.id, myLocator).__getitem__().__len__()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def getContentDescription(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).get_attribute("content-Desc")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def getName(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).get_attribute("name")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def getLocation(self, myLocator, locatorType):
        try:
            self.getElement(myLocator, locatorType).location
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger(error)

    def clickListElement(self, myLocator, locatorType, elementPosition, element=None):
        try:

            if element is None:
                element = self.getElements(myLocator,locatorType).__getitem__(elementPosition)
                #element = self.waitForElementToBeClickable(myLocator, locatorType)
            element.click()
                #self.getElements(myLocator, locatorType).__getitem__(elementPosition).click()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.takescreenShotOnError()
            self.logger(error)

    def waitForElementToBeClickable(self, myLocator, locatorType, timeout=35, poll_frequency=.5, elt=None):
        try:
            wt = WebDriverWait(self.driver,timeout,poll_frequency,
                                    ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                        ElementNotSelectableException])
            byType = self.getByType ( locatorType)
            element = wt.until(e_c.element_to_be_clickable(byType, myLocator))
            self.logger.info(f"waiting for {element} to be clickable")
            return element
        except Exception as error:
            self.logger.error(error)

    def scrollDownToBottom(self):
        try:
            windowHeight = self.driver.execute_script("retrun document.body.scrollHeight);")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                newWidowHeight = self.driver.execute_script("retrun document.body.scrollHeight);")
                if windowHeight == newWidowHeight:
                    break
                windowHeight=newWidowHeight
        except Exception as error:
            self.logger(error)

    def scrollUpToTop(self):
        try:
            windowHeight = self.driver.execute_script("retrun document.body.scrollHeight);")
            while True:
                self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

                newWidowHeight = self.driver.execute_script("retrun document.body.scrollHeight);")
                if windowHeight == newWidowHeight:
                    break
                windowHeight = newWidowHeight
        except Exception as error:
            self.logger(error)

    def scrollElementIntoView(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as error:
            self.logger(error)


    def scrollDownToElement(self, element):
        try:
            element.send_keys(Keys.PAGE_DOWN)
        except Exception as error:
            self.logger(error)

    def scrollUpToElement(self, element):
        try:
            element.send_keys(Keys.PAGE_UP)
        except Exception as error:
            self.logger(error)

    def goBack(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ALT, Keys.LEFT).perform()
        except Exception as error:
            self.logger(error)

    def moveMouseOnElement(self, mylocator, locatorType):
        try:
            actions = ActionChains(self.driver)
            byType = self.getByType(locatorType)
            element = self.getElement(mylocator, locatorType)
            actions.move_to_element(element).perform()
        except Exception as error:
            self.takescreenShotOnError()
            self.logger.error(error)
        #finally:
            #self.takescreenShotOnError()


    def takescreenShotOnError(self, stepname="click"):
        try:
            tsp = time.time().__str__() #datetime.now()
            #self.logger.warn(tsp)
            name=stepname+tsp+".png"

            self.driver.save_screenshot(name)
            #webdriver.Chrome.get.get_screenshot_as_png()
            self.logger.info("taking screenshot ... "+name)
        except Exception as error:
            self.logger.error ( "Error could not take screenshot")
            self.logger.error(error)

