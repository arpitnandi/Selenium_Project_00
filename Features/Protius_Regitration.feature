# Created by arpit.nandi at 2019-03-27
Feature: Protius Discover App registration feature

  Scenario: Try to register without 4 digit PIN
    Given Login page is open
    When User clicks on Register button
    Then Enters validUser9@protius.com and mpbile
    And Enters PP1234, Stan, Lee, 1234567890 and 8/8/1980
    And Provides a 1234567890 and skips from PIN
    When User is on Dashboard
    Then Clicks on menue
    And Clicks on profile
    And Go for change the old password
    And Enters current 1234567890
    And Enters New 0987654321
    And Clicks on back button
    When User is on dashboard
    Then Clicks on signout
    And Clicks on confirm
    And Comes to loggin page
    And Closes application