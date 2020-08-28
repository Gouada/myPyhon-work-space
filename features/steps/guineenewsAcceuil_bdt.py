from time import sleep

from behave import *
from pages.guineenewsAcceuilPage import GuineenewsAcceuil


class Guineenews_BDT ():

    @fixture
    def initialization(context):
        context.acceuil_page = GuineenewsAcceuil ( context.driver )

    def before_step(context):
        use_fixture( context.initialization, context )

    @when ( 'I scroll to rubrique "{rubrique}"' )
    def step_impl(context, rubrique):
        try:
            context.acceuil_page = GuineenewsAcceuil ( context.driver )
            context.acceuil_page.scroll_to_rubrique ( rubrique )
            assert context.acceuil_page.is_text_present(rubrique)
            sleep(3)
        except (Exception, AssertionError) as error:
            context.logger.error(error)
            raise AssertionError (error)

    @then('I open "{position}" "{rubrique}" article')
    def step_impl(context, position, rubrique):
        try:
            context.acceuil_page.click_a_rubrique_element(rubrique, position)
            #context.logger.info ( rubrique + " ......Title: ....." + context.acceuil_page.getPageTitle () )
            assert context.acceuil_page.is_text_present ( "Accueil" )
            #assert context.acceuil_page.is_rubrique_tag_on_page(rubrique)
            sleep ( 3 )
        except AssertionError as error:
            context.logger.error ( "AssertionError: " + rubrique + " was not found on page " + error.__str__() )
            raise AssertionError( "AssertionError: " + rubrique + " was not found on page " + error.__str__() )

