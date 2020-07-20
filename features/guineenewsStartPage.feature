Feature: showing off behave

  Scenario: run a simple test
     Given I start the site guineenews
      When I click on politique
      Then I click on societe
      Then I click a random Region
      Then I click a random grands dossiers
      Then I click a random publireportage
