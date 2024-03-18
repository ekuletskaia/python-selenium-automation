Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Tea into search field
    And Click on search icon
    Then Product results for Tea are shown