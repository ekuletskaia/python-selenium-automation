from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ITEMS_IN_CART = (By.CSS_SELECTOR, 'span[class*=CartSummary]')


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_is_empty(context):
    # actual_text = context.driver.find_element(*TEXT_CART_EMPTY).text
    # assert "Your cart is empty" in actual_text, f'Error! text "Your cart is empty" not in {actual_text}'
    context.app.cart_page.verify_cart_empty_msg()


@then('Verify {item} is in the cart')
def verify_item(context, item):
    context.driver.find_element(*ITEMS_IN_CART)
