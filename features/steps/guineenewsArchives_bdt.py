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
            assert context.archivesPage.is_text_present("Archives ")
        except (Exception, AssertionError) as error:
            context.logger.error ( error )

    @then ( u'I open "{pos}" article on result page' )
    def step_impl(context, pos):
        try:
            if pos.upper() == "FIRST":
                context.searchPage.click_a_specific_search_result ( 0 )
            if pos.upper() == "LAST":
                context.searchPage.click_a_specific_search_result ( "last" )
            if pos.upper() == "RANDOM":
                context.searchPage.click_a_random_search_result ()
            assert context.searchPage.is_text_present("ECOUTEZ LA RADIO ESPACE FM")
            sleep(3)
        except (Exception, AssertionError) as error:
            context.logger.error ( error )

    @when ( u'I go to "{mnt}" month' )
    def step_impl(context, mnt):
        try:
            context.archivesPage = GuineenewsArchivesPage ( context.driver )
            if mnt == "previous":
                context.archivesPage.click_previous_month()
            else:
                context.archivesPage.click_next_month()

            assert context.searchPage.is_text_present ( "Archives mensuelles: " )
        except (Exception, AssertionError) as error:
            context.logger.error ( error )

    @then ( u'I paginate to "{num}" page' )
    def step_impl(context, num):

        try:
            if num == "last":
                context.searchPage.paginate_to_last_result_page()
            assert "page" in context.searchPage.getCurrentUrl()
        except (Exception, AssertionError) as error:
            context.logger.error ( error )