Feature: search and read an article

  Background:
     Given I start guineenews

  @wip
  Scenario: les articles en vedette
       Then I go to sub category economy
       Then I select les plus populaires
       Then I select randomly one article
       Then I go back

  @wip
  Scenario Outline: search article
      When I search "<word>"
      Then I scroll to bottom
      Then I check if there more than one page
      Then I paginate to next page
      Then I scroll to top
      Then I select randomly one result
      Then I go back to search result
      Then I select randomly another result
      Then I go to start page

      Examples: Test data
          | word           |
          | Alpha Conde   |
          | Cellou Dalein  |
          | KPC            |
