Feature: search and read an article

  Background:
     Given I start guineenews

 @wip
  Scenario Outline: les articles populaire
       Then I scroll to "top"
       Then I go to sub category "<cat>"
       Then I select les plus populaires
       Then I select randomly one article
       Then I click page "down" button
       Then I go back
   Examples:
     |cat       |
     |Economy   |
     |Politique |
     |Societe   |

  Scenario Outline: search article
      Then I scroll to "top"
      When I search "<word>"
      Then I scroll to "bottom"
      Then I check if there more than one page
      Then I paginate to next page
      Then I scroll to "top"
      Then I select randomly one result
      Then I click page "down" button
      Then I go back to search result
      Then I select randomly one result
      Then I click page "down" button
      Then I click page "up" button
      Then I go to start page

      Examples: Test data
          | word           |
          | Alpha Conde   |
          | Cellou Dalein  |
          | KPC            |

  Scenario Outline: les articles en vedette
       Then I scroll to "top"
       Then I go to sub category "<cat>"
       Then I select les articles en vedette
       Then I select randomly one article
       Then I scroll to "bottom"
       Then I go back
   Examples:
     |cat       |
     |Economy   |
     |Politique |
     |Societe   |
