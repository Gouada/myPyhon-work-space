Feature: search and read an article

  Background:
     Given I start the site guineenews

  Scenario Outline: search article
      When I search <word>
      Then I scroll to bottom
      Then I check if there more than one page
      Then I scroll to top
      Then I scroll down
      Then I select randomly one result
      Then I go back to search result
      Then I select randomly another result
      Then I go to start page

   Examples:
    | word           |
    | Alpaha Conde   |
    | Cellou Dalein  |
    | KPC            |

  Scenario: les articles en vedette
       When I go to sub category economy
       Then I slect les plus populaires
       Then I select randomly one article
       Then I go back
