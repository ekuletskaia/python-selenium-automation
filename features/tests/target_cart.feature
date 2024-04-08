# Created by elena.kuletsky at 4/2/2024
Feature: Cart tests

  Scenario: Verify Cart Functionality
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown