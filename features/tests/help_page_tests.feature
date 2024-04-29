# Created by elena.kuletsky at 4/7/2024
Feature: Target Help page UI

  Scenario: Verify main elements are shown
    Given Open Help page
    Then Title 'Target Help' is shown
    Then Search field is shown
    Then Search button is shown
    Then Section_1 with 7 elements is shown
    Then Section_2 with 2 elements (contact us and product recalls) is shown
    Then Title "Browse all Help pages" is shown

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page opened

  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Target Circle™
    Then Verify About Target Circle page opened

  Scenario: User can select Help topic Nutrition Information
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Nutrition Information
    Then Verify Bakery page opened