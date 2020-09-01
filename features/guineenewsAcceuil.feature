@fixture.initialization
Feature: Acceuil

  Background: Start guineenews.org
    Given I start guineenews

  @acceuil
  Scenario Outline: scrolling through

    When I scroll to rubrique "<rubrique>"
    Then I open "0" "<rubrique>" article
    #Then I click page "down" button
    Then I go back
    Then I open "last" "<rubrique>" article
    #Then I click page "down" button
    Then I go back
    Then I open "random" "<rubrique>" article
    #Then I click page "down" button
    Then I go back
    Examples:
      | rubrique        |
      | POLITIQUE       |
      | ECONOMIE        |
      | REVUE DE PRESSE |
      | SPORT           |
      | SOCIETE         |
      | INTERVIEW       |
      | LE MONDE        |
      | ART   |
      | DERNIERES NOUVELLES |
      | PUBLIREPORTAGE   |
      | FAITS DIVERS     |


