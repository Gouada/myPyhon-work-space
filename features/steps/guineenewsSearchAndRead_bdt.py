from time import sleep

from behave import *
from pytest import fail

from constants.guineenewsMenu_cats import Menu
from pages.guineenewsSerachPage import GuineenewsSearchPage

from constants.urls import Urls
from pages.guineenewsMenu import GuineenewsMenu

class SerachAndReadArticle():

    # @fixture(name="init")
    # def initialize(context):
    #     context.menu = GuineenewsMenu ( context.driver )
    #     context.searchPage = GuineenewsSearchPage ( context.driver )

    @given('I start guineenews')
    def step_impl(context):
        try:
            context.driver.get(Urls.startPage_guineenews)
            context.menu = GuineenewsMenu ( context.driver )
            context.searchPage = GuineenewsSearchPage ( context.driver )
            sleep(2)
        except Exception as error:
            context.logger.error(error)
            fail ( 'Step fail with {}'.format ( str ( error ) ) )

    @when('I search "{word}"')
    def step_impl(context, word):
        try:
            context.menu.search(word)
            sleep ( 3 )
            noResults = "Aucun résultat pour votre recherche"
            assert not context.searchPage.is_text_present(noResults)
        except Exception as error:
            context.logger.error(error)

    @then('I check if there more than one page')
    def step_impl(context):
        try:
            assert context.searchPage.is_more_than_one_result_page()
        except Exception as error:
            context.logger.error(error)

    @then ( 'I scroll to top' )
    def step_impl(context):
        try:
            context.searchPage.scrollUpToTop()
            sleep(3)
        except Exception as error:
            context.logger.error(error)

    @then ( 'I paginate to next page' )
    def step_impl(context):
        try:
            context.searchPage.paginate_to_next_Page()
            sleep(5)
        except Exception as error:
            context.logger.error(error)

    @then ( 'I select randomly one result' )
    def step_impl(context):
        try:
            context.searchPage.click_a_random_search_result()
            sleep(5)
        except Exception as error:
            context.logger.error(error)

    @then ( 'I go back to search result' )
    def step_impl(context):
        try:
            context.searchPage.goBack()
        except Exception as error:
            context.logger.error(error)

    @then ( 'I select randomly another result' )
    def step_impl(context):
        try:
            context.searchPage.click_a_random_search_result()
        except Exception as error:
            context.logger.error(error)

    @then ( 'I go to start page' )
    def step_impl(context):
        try:
            context.menu.click_logo()
        except Exception as error:
            context.logger.error(error)

    @then ( 'I go to sub category economy' )
    def step_impl(context):
        try:
            context.menu.go_to_news_sub_rubrique ( Menu.Economie )
            sleep ( 3 )
        except Exception as error:
            fail ( 'Step fail with {}'.format ( str ( error ) ) )
            context.logger.error ( error )
            context.startPage.takescreenShotOnError ( "I_go_to_sub_category_economy" )\

    @then ( 'I select les plus populaires' )
    def step_impl(context):
        try:
            context.menu.select_from_derniers_drop_down_Menu ( Menu.Filter_cretaria_plus_populaire )
            sleep ( 3 )
        except Exception as error:
            context.logger.error ( error )

    @then ( u'I select randomly one article' )
    def step_impl(context):
        try:
            context.searchPage.click_a_random_search_result ()
        except Exception as error:
            context.logger.error ( error )

    @then ( u'I go back' )
    def step_impl(context):
        try:
            context.searchPage.goBack ()
        except Exception as error:
            context.logger.error ( error )

    @then ( 'I scroll to bottom' )
    def step_impl(context):
        try:
            context.menu.scrollDownToBottom ()
            sleep ( 1 )
        except Exception as error:
            context.logger.error(error)
