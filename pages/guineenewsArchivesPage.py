

from pages.basePage import BasePage

class GuineenewsArchivesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    calendar_table_id = "wp-calendar"
    calendar_day_having_archives = "//table[@id='wp-calendar']//child::a[contains(@aria-label, 'Publications')]"
    previous_month = "//nav[@class='wp-calendar-nav']/span[@class='wp-calendar-nav-prev']/a"
    next_month = "//nav[@class='wp-calendar-nav']/span[@class='wp-calendar-nav-next']/a"

    def select_archives(self, day):
        day_index = (int(day)-1)
        element = self.getListElement(myLocator=self.calendar_day_having_archives,locatorType="xpath",elementPosition=day_index)
        #self.scrollElementIntoView(element)
        self.clickListElement(myLocator=self.calendar_day_having_archives,locatorType="xpath",elementPosition=day_index)
