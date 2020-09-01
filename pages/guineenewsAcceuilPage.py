
from pages.basePage import BasePage
from utils.logger import MyLogger
from constants.guineenewsMenu_cats import Menu
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

    rubrique_tags = "//ul[@class='td-category']/li"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_rubrique_tag_on_page(self, rubrique):
        rubriques = self.getElements(self.rubrique_tags, "xpath")
        if Menu.Le_Monde.upper() == rubrique.upper() or Menu.Societe_sa.upper() == rubrique:
            return True
        elif len(rubriques) > 0:
            for r in rubriques:
                if self.getElementText(element=r).upper() == rubrique.upper():
                    return True
            return False
        else:
            return False
    def get_rubrique_xpath(self, rubrique):

        if rubrique == 'PUBLIREPORTAGE':
            return "//div[@class='td-block-title-wrap']//child::span[contains(text(), '{}')]".format(str(rubrique).upper())
        else:
            return "//div[@class='td-block-title-wrap']//child::a[contains(text(), '{}')]".format(str(rubrique).upper())

    def get_rubrique_elements_xpath_locaor(self, rubrique):
        #myLocator = "//div[@id='{}']//child::div[@class='item-details']//a".format(str(rubrique_div_id))
        if rubrique.upper() == 'PUBLIREPORTAGE':
            myLocator = "//div[@class='td-block-title-wrap']//child::span[contains(text(), '{}')]/ancestor::div[@class='td-block-title-wrap']//" \
                        "following-sibling::div[@class='td_block_inner']//child::h3[@class='entry-title td-module-title']//a" \
                .format ( str ( rubrique ).upper () )
        else:
            myLocator = "//div[@class='td-block-title-wrap']//child::a[contains(text(), '{}')]/ancestor::div[@class='td-block-title-wrap']//" \
                    "following-sibling::div[@class='td_block_inner']//child::h3[@class='entry-title td-module-title']//a"\
                .format(str(rubrique).upper())
        return myLocator

    def scroll_to_rubrique(self, rubrique, locatorType="xpath"):

        myLocator = self.get_rubrique_xpath(rubrique)
        element = self.getElement(myLocator, locatorType)
        self.moveToElement(element)
        if rubrique.upper() == "POLITIQUE" or rubrique.upper() == "ART":
            self.arrow_down_up(3, "down")


    def click_a_rubrique_element(self, rubrique, element_index_str=None):

        myLocator = self.get_rubrique_elements_xpath_locaor(rubrique)
        elements = self.getElements(myLocator=myLocator, locatorType="xpath")
        if element_index_str == "random":
            element_index = random.randint(0, int(len(elements) -1))
            element = self.getListElement ( myLocator=myLocator, locatorType="xpath",
                                            elementPosition=int ( element_index ) )
            self.moveToElement(element)
        elif element_index_str == "last":
            element_index = int(len(elements) -1)
        else:
            element_index = int(element_index_str)

        #if self.isVisible(element=element) is False or self.isClickable(element=element) is False:
            #self.arrow_down_up(3,"UP")
            #self.logger.warning("element was not visible i scrolled")
        self.clickListElement(elements=elements,elementPosition=int(element_index))

