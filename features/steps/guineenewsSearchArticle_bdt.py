from time import sleep

from behave import *
from pytest import fail
from pages.guineenewsSerachPage import GuineenewsSearchPage

from constants.urls import Urls
from pages.guineenewsMenu import GuineenewsMenu
import pytest

class SerachAndReadArticle():


    # @given('I start the site guineenews')
    # def step_impl(context):
    #     try:
    #         context.driver.get(Urls.startPage_guineenews)
    #     except Exception as error:
    #         context.logger.error(error)
    #         fail ( 'Step fail with {}'.format ( str ( error ) ) )

    @pytest.fixture(autouse=True)
    def initialize(context):
        context.menu = GuineenewsMenu ( context.driver )
        context.searchPage = GuineenewsSearchPage ( context.driver )

    @when("I search '{word}' ")
    def step_impl(context, word):
        context.menu.search(word)
        sleep ( 2 )
        noResults = "Aucun * pour votre recherche"
        assert noResults not in context.response

    @then ('I scroll to bottom')
    def step_impl(context):
        context.menu.scrollDownToBottom()
        sleep(2)

    @then('I check if there more than one page')
    def step_impl(context):
        assert context.searchPage.is_more_than_one_result_page()

    @then ( u'I scroll to top' )
    def step_impl(context):
        context.searchPage.scrollUpToTop()

    @then ( u'I scroll down' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I scroll down' )

    @then ( u'I select randomly one result' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I select randomly one result' )

    @then ( u'I go back to search result' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I go back to search result' )

    @then ( u'I select randomly another result' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I select randomly another result' )

    @then ( u'I go to start page' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I go to start page' )


    @when ( u'I go to sub category economy' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: When I go to sub category economy' )

    @then ( u'I slect les plus populaires' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I slect les plus populaires' )

    @then ( u'I select randomly one article' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I select randomly one article' )

    @then ( u'I go back' )
    def step_impl(context):
        raise NotImplementedError ( u'STEP: Then I go back' )



