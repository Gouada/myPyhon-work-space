from datetime import datetime

import now as now
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.actions import *obj9ob9
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
        #webdriver.Chrome.
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
            #self.logger.info(byType)
            el = self.driver.find_element(byType, myLocator)
            return el
        except (Exception, NoSuchElementException) as error:
            self.logger.error(error)

    def getElements(self, myLocator, locatorType="id"):
        """
        :type locator: string
        """
        try:
            byType = self.getByType(locatorType)
            el = self.driver.find_elements(byType, myLocator)
            return el
        except (Exception, NoSuchElementException) as error:
            self.logger.error(error)

    def clickElement(self, myLocator="None", locatorType="id", element=None):
        try:
            if element is None:
                element = self.getElement(myLocator, locatorType)
            element.click()
        except ElementNotVisibleException as error:
            self.logger.error(str(error))

    def typeTextInField(self, myLocator='', locatorType="id",text='', element=None):
        try:
            if element is None:
                element = self.getElement(myLocator, locatorType)
            element.send_keys(text)
        except ElementNotVisibleException as error:
            self.logger.error(error)

    def clearField(self, myLocator='', locatorType='id',element=None):
        try:
            if element is None:
                element = self.getElement(myLocator, locatorType)
            element.clear()
        except ElementNotVisibleException as error:
            self.logger.error(error)

    def getElementText(self, myLocator="", locatorType="", element=None):
        try:
            if element is None:
                    element = self.getElement(myLocator, locatorType)
            return element.text
        except ElementNotVisibleException as error:
            self.logger.error(error)

    def getPageTitle(self):
        try:
            return self.driver.title
        except Exception as error:
            self.logger.error(error)

    def getCurrentUrl(self):
        try:
            return  self.driver.current_url
        except Exception as e:
            self.logger.error(e.__str__())

    def getTagName(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).tag_name
        except ElementNotVisibleException as error:
            self.logger.error(error)

    def isEnabled(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).is_enabled()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def isVisible(self, myLocator="", locatorType="xpath", element=None):
        is_visible=True
        try:
            if element is None:
                element = self.getElement(myLocator, locatorType)
            is_visible=element.is_displayed()
            self.logger.warning("checking element visibility"+is_visible)
            return is_visible
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def isSelected(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).is_selected()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    #def isEmpty(self, myLocator, locatorType):
     #   self.getElement(myLocator, locatorType).

    def isChecked(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).get_attribute("checked")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def isFocused(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).get_attribute("focused")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def isClickable(self, myLocator="", locatorType="xpath", element=None):
        is_clickable=True
        try:
            if element is None:
                byType = self.getByType(locatorType)
                element = self.getElement(myLocator, byType)
            is_clickable = element.get_attribute("clickable")
            self.logger.warning ( "checking element visibility" + is_clickable )
            return is_clickable
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def selectElementDropDownElement(self, myLocator=None, locatorType="xpath", value=None, index=None, text=None, criteria="value", element=None):
        try:
            if element is None:
                element = self.getElement(myLocator,locatorType)
            if criteria == "value":
                return Select(element).select_by_value(value)
            if criteria == "index":
                return Select ( element ).select_by_index(index)
            if criteria == "text":
                return Select ( element ).select_by_visible_text(text)
        except Exception as error:
            self.logger.error(error)

    def deselectDropDownElement(self, myLocator=None, locatorType="xpath", value=None, index=None, text=None,
                             criteria="value", element=None):
        try:
            if element is None:
                element = self.getElement ( myLocator, locatorType )
            if criteria == "value":
                return Select ( element ).select_by_value ( value )
            if criteria == "index":
                return Select ( element ).select_by_index ( index )
            if criteria == "text":
                return Select ( element ).select_by_visible_text ( text )
        except Exception as error:
            self.logger.error ( error )

    def isListElementClickable(self, myLocator=None, locatorType="xpath", position=None, element=None):
        try:
            if element is None:
                byType = self.getByType(locatorType)
                element = self.getElements(myLocator, byType).__getitem__(position)
            return element.get_attribute("clickable")
        except Exception as error:
            self.logger.error(error)

    def getClassName(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).get_attribute("classname")
            #webdriver.Chrome.find_elements(By.id, myLocator).__getitem__().__len__()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def getContentDescription(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).get_attribute("content-Desc")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def getName(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).get_attribute("name")
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def getLocation(self, myLocator, locatorType):
        try:
            return self.getElement(myLocator, locatorType).location
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.logger.error(error)

    def is_text_present(self, text):
        try:
            return str ( text ) in self.driver.page_source
        except ElementNotVisibleException as error:
            self.logger.error(error)

    def clickListElement(self, myLocator=None, locatorType="xpath", elementPosition=0, element=None, elements=None):
        try:
            if elements is not None:
                element = elements.__getitem__(elementPosition)

            elif element is None and myLocator is not None:
                element = self.getElements(myLocator,locatorType).__getitem__(elementPosition)
                #element = self.waitForElementToBe(myLocator, locatorType)
            element.click()
                #self.getElements(myLocator, locatorType).__getitem__(elementPosition).click()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.takescreenShotOnError()
            self.logger.error(error)

    def getListElement(self, myLocator=None, locatorType="xpath", elementPosition=0, element=None):
        try:

            if element is None:
                element = self.getElements(myLocator,locatorType).__getitem__(elementPosition)
                #element = self.waitForElementToBe(myLocator, locatorType)
            return element
                #self.getElements(myLocator, locatorType).__getitem__(elementPosition).click()
        except (ElementNotSelectableException, ElementNotVisibleException) as error:
            self.takescreenShotOnError()
            self.logger.error(error)

    def waitForElementToBe(self, myLocator, locatorType="xpath", timeout=15, poll_frequency=.5, element=None, event="clickable"):
        try:
            #wt = WebDriverWait(self.driver,10)
            wt = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency,
                                    ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                        ElementNotSelectableException, ElementNotInteractableException])
            byType = self.getByType ( locatorType)

            if event == 'visible':
                element = wt.until(EC.presence_of_element_located((byType, myLocator)))
            if event == "clickable":
                element = wt.until(EC.element_to_be_clickable((byType, myLocator)))
            else:
                element = wt.until(EC.element_to_be_clickable((byType, myLocator)))
            return element
        except Exception as error:
            self.logger.error(str(error))

    def scrollDownToBottom(self):
        try:
            windowHeight = self.driver.execute_script("return document.body.scrollHeight;")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                newWidowHeight = self.driver.execute_script("return document.body.scrollHeight;")
                if windowHeight == newWidowHeight:
                    break
                windowHeight=newWidowHeight
        except Exception as error:
            self.logger.error(error)

    def scrollUpToTop(self):
        try:
            windowHeight = self.driver.execute_script("return document.body.scrollHeight;")
            while True:
                self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

                newWidowHeight = self.driver.execute_script("return document.body.scrollHeight;")
                if windowHeight == newWidowHeight:
                    break
                windowHeight = newWidowHeight
        except Exception as error:
            self.logger.error(error)

    def scrollElementIntoView(self, element):
        try:
            #self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            actions = ActionChains ( self.driver )
            actions.move_to_element(element).perform()
        except Exception as error:
            self.logger.error(error)

    def scrollDownToElement(self, element):
        try:
            element.send_keys(Keys.PAGE_DOWN)
        except Exception as error:
            self.logger.error(error)

    def scrollUpToElement(self, element):
        try:
            element.send_keys(Keys.PAGE_UP)
        except Exception as error:
            self.logger.error(error)

    def pageDown(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
        except Exception as error:
            self.logger.error(error)

    def pageUp(self):
        try:
            actions = ActionChains ( self.driver )
            actions.send_keys ( Keys.PAGE_UP ).perform ()
        except Exception as error:
            self.logger.error(error)

    def arrow_down_up(self, count, direction):
        actions = ActionChains ( self.driver )
        i = 0
        try:
            if direction.upper() == "DOWN":
                while i < int(count):
                    actions.send_keys ( Keys.ARROW_DOWN ).perform ()
                    time.sleep ( 2 )
                    i =i+1
            elif direction.upper() == "UP":
                while i < int ( count ):
                    actions.send_keys ( Keys.ARROW_UP ).perform ()
                    time.sleep ( 2 )
                    i = i+1
        except Exception as error:
            self.logger.error(error)

    def goBack(self):
        try:
            last_height = self.driver.execute_script ( "return document.body.scrollHeight" )
            self.driver.execute_script ( "window.scrollTo(0, document.body.scrollHeight);" )
            self.driver.execute_script ( "window.history.go(-1)" )

            #actions = ActionChains(self.driver)
            #actions.send_keys(Keys.ALT, Keys.LEFT).perform()
            #actions.key_down(Keys.ALT).send_keys(Keys.LEFT).key_up(Keys.ALT).perform()
        except Exception as error:
            self.logger.error(error)

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
            #webdriver.Chrome.get_screenshot_as_png()
            self.logger.info("taking screenshot "+name)
        except Exception as error:
            self.logger.error ( "Error could not take screenshot")
            self.logger.error(error)

