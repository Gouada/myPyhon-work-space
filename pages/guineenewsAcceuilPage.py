
from pages.basePage import BasePage
from utils.logger import MyLogger
import logging
import random

class GuineenewsAcceuil(BasePage):

    mylg = MyLogger()
    logger = mylg.customLogger(logging.DEBUG)

    # rubrique_title_dernieres_novelles   = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'DERNIERES NOUVELLES')]"
    # rubrique_title_politique            = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'POLITIQUE')]"
    # rubrique_title_Publi_reportage      = "//div[@class='td-block-title-wrap']//child::span[contains(text(), 'PUBLIREPORTAGE')]"
    # rubrique_title_Grand_Dossiers       = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'GRANDS DOSSIERS')]"
    # rubrique_title_Grand_Economie       = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'ECONOMIE')]"
    # rubrique_title_Grand_Sport          = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'SPORT')]"
    # rubrique_title_Grand_Societe        = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'SOCIETE')]"
    # rubrique_title_Grand_Dossiers       = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'GRANDS DOSSIERS')]"
    # rubrique_title_Grand_Economie       = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'ECONOMIE')]"
    # rubrique_title_Grand_Sport          = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'SPORT')]"
    # rubrique_title_Grand_Societe        = "//div[@class='td-block-title-wrap']//child::a[contains(text(), 'SOCIETE')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_rubrique_xpath(self, rubrique):

        if rubrique == 'PUBLIREPORTAGE':
            return "//div[@class='td-block-title-wrap']//child::span[contains(text(), '{}')]".format(str(rubrique).upper())
        else:
            return "//div[@class='td-block-title-wrap']//child::a[contains(text(), '{}')]".format(str(rubrique).upper())

    def get_rubrique_elements_xpath_locaor(self, rubrique):

        #myLocator = "//div[@id='{}']//child::div[@class='item-details']//a".format(str(rubrique_div_id))
        myLocator = "//div[@class='td-block-title-wrap']//child::a[contains(text(), '{}')]/ancestor::div[@class='td-block-title-wrap']//" \
                    "following-sibling::div[@class='td_block_inner']//child::h3[@class='entry-title td-module-title']//a"\
            .format(str(rubrique).upper())
        return myLocator

    def scroll_to_rubrique(self, rubrique, locatorType="xpath"):

        myLocator = self.get_rubrique_xpath(rubrique)
        element = self.getElement(myLocator, locatorType)
        self.scrollElementIntoView(element)

    def click_a_rubrique_element(self, rubrique, element_index_str=None):

        myLocator = self.get_rubrique_elements_xpath_locaor(rubrique)
        elements = self.getElements(myLocator=myLocator, locatorType="xpath")
        if element_index_str == "random":
            element_index = random.randint(0, len(elements))
        elif element_index_str == "last":
            element_index = int(len(elements) -1)
        else:
            element_index = int(element_index_str)
        self.clickListElement(elements=elements,elementPosition=int(element_index))
