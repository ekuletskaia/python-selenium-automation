from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_HEADER = (By.XPATH, '//div[@data-test="resultsHeading"]')
ADD_TO_CART_BTN1 = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor82394015')
ADD_TO_CART_BTN2 = (By.CSS_SELECTOR, 'button[data-test="shippingButton"]')
VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[href="/cart"]')
ITEMS_IN_CART = (By.CSS_SELECTOR, 'span[class*=CartSummary]')


@then("Verify search results are shown for {expected_item}")
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'


@when('Add product to Cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN1).click()
    sleep(4)
    context.driver.find_element(*ADD_TO_CART_BTN2).click()
    context.driver.find_element(*VIEW_CART_BTN).click()


@then('Verify {item} is in the cart')
def verify_item(context, item):
    context.driver.find_element(*ITEMS_IN_CART)
