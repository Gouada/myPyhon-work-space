from behave import when, then
from pages.guineenewsArchivesPage import GuineenewsArchivesPage
from pages.guineenewsMenu import GuineenewsMenu
from pages.guineenewsSerachPage import GuineenewsSearchPage

class GuineenewsArchives():

    @when ( 'I select the archives of specific "{day}"' )
    def step_impl(context, day):
        try:
            context.archivesPage =  GuineenewsArchivesPage(context.driver)
            context.menuPage  =  GuineenewsMenu(context.driver)
            context.searPage = GuineenewsSearchPage(context.driver)
            context.archivesPage.select_archives(day)
        except Exception as error:
            context.logger.error(error)

    @then ( u'I open "{pos}" article of that day' )
    def step_impl(context, pos):

        if pos.upper == "FIRST":
            context.searPage.click_a_specific_search_result(0)
        if pos.upper == "LAST":
            context.searPage.click_a_specific_search_result("last")
        if pos.upper == "RANDOM":
            context.searPage.click_a_random_search_result()


