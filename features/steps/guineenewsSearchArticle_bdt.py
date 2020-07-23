

from behave import *
from pytest import fail

from constants.urls import Urls
from pages.guineenewsMenu import GuineenewsMenu
class SerachAndReadArticle():


    @given('I start the site guineenews')
    def step_impl(context):
        try:
            context.driver.get(Urls.startPage_guineenews)
            context.menu = GuineenewsMenu(context.driver)
        except Exception as error:
            context.logger.error(error)
            fail ( 'Step fail with {}'.format ( str ( error ) ) )

    @then('I search {word}')
    def step_impl(context, word):
        context.menu.search(word)
        noResults = "Aucun * pour votre recherche"
        assert noResults not in context.response

    @then ('I scroll to bottom')
    def step_impl(context):
        context.menu.scrollDownToBottom()

    @then('I check if there more than one page')
    def step_impl(context):
        

