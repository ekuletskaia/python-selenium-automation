# Created by elena.kuletsky at 4/2/2024
Feature: Sign In

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open target.com
    When Click Sign In
    Then Verify Sign In form opened