
Feature:  read articles

  Background: start guineenews
    Given I start guineenews
  @test
  Scenario Outline: read archives of defined day
    Then I scroll to "bottom"
    When I select the archives of specific "<day>"
    Then I open "first" article on result page
    Then I click page "down" button
    Then I go back
    Then I open "last" article on result page
    Then I click page "down" button
    Then I go back
    Then I open "random" article on result page
    Then I click page "down" button
    Then I go back
    Examples:
      | day |
      | 1   |
      | 10  |

  @test
  Scenario: read previous month archive
    When I go to "previous" month
    Then I paginate to "last" page
    Then I open "first" article on result page
    Then I click page "down" button
    Then I go back
    Then I open "last" article on result page
    Then I click page "down" button
    Then I click page "up" button