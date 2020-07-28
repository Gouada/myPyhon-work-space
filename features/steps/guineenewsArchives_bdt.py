from time import sleep

from behave import when, then
from pages.guineenewsArchivesPage import GuineenewsArchivesPage
from pages.guineenewsMenu import GuineenewsMenu
from pages.guineenewsSerachPage import GuineenewsSearchPage


class GuineenewsArchives ():

    @when ( 'I select the archives of specific "{day}"' )
    def step_impl(context, day):
        try:
            context.archivesPage = GuineenewsArchivesPage ( context.driver )
            context.menuPage = GuineenewsMenu ( context.driver )
            context.searchPage = GuineenewsSearchPage ( context.driver )

            context.archivesPage.select_archives ( day )
        except Exception as error:
            context.logger.error ( error )

    @then ( u'I open "{pos}" article of that day' )
    def step_impl(context, pos):
        try:
            if pos.upper() == "FIRST":
                context.searchPage.click_a_specific_search_result ( 0 )
            if pos.upper() == "LAST":
                context.searchPage.click_a_specific_search_result ( "last" )
            if pos.upper() == "RANDOM":
                context.searchPage.click_a_random_search_result ()
            sleep(3)
        except Exception as error:
            context.logger.error(error)