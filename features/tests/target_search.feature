# Created by elena.kuletsky at 4/6/2024
Feature: Search tests

  Scenario: Verify product in the cart after click "Add to Cart"
    Given Open target.com
    When Search for mug
    When Add product to Cart
    Then Verify mug is in the cart


  Scenario Outline: User can search for product
    Given Open target.com
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item        |expected_item   |
    |coffee      |coffee          |
    |tea         |tea             |
    |mug         |mug             |

  Scenario: Verify that every product on Target search results
  page has a product name and product image
    Given Open target.com
    When Search for chair
    Then Verify search results display product name and product image
    Then Verify URL has chair