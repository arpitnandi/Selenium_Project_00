# Created by arpit.nandi at 2019-03-25
Feature: Test the Search feature

  @First
  Scenario: test with single word
    Given User is on http://google.com
    When User enters the search Automation
    Then User clicks on search button
    And User selects all links from search result
    And User cleare the Search edit text
    And User closes the window

  @Second
  Scenario: test with Sentance
     Given User is on http://google.com
     When User enters the search Python Automation
     Then User clicks on search button
     And User selects all links from search result
     And User cleare the Search edit text
     And User closes the window