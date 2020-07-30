from behave import *
from pages.guineenewsAcceuilPage import GuineenewsAcceuil


class Guineenews_BDT ():

    def __init__(context):
        context.acceuil_page = GuineenewsAcceuil ( context.driver )

    @when ( "I scroll to rubrique '{rubrique}'" )
    def step_impl(context, rubrique):
        context.acceuil_page.scroll_to_rubrique ( rubrique )

    @then("I open '{position}' '{rubrique}' article")
    def step_impl(context, position, rubrique):
        context.acceuil_page.click_a_rubrique_element(rubrique, position)