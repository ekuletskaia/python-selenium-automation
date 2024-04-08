# Created by elena.kuletsky at 4/7/2024
Feature: Tests for main page UI


  Scenario: Verify header is shown
    Given Open target.com
    Then Verify header is shown

  Scenario: Verify header has correct amount links
    Given Open target.com
    Then Verify header has 6 links