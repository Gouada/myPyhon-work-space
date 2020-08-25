Feature: showing off behave
@sp
  Scenario: test 1
     Given I start the site guineenews
     Then I click on Societe
      Then I click a random Region
      Then I scroll to "top"
      Then I click a random grands dossiers
      Then I scroll to "top"
      Then I click page "down" button
      When I click on politique
      Then I scroll to "top"
      Then I click a random publireportage
      Then I scroll to "top"
