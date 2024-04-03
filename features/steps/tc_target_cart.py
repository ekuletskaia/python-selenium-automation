from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open target.com")
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Click on Cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test*='CartIcon']").click()
    sleep(5)

@then("Verify “Your cart is empty” message is shown")
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert "Your cart is empty" in actual_text, f'Error! text "Your cart is empty" not in {actual_text}'
    print("Test case passed.")

@when("Click Sign In")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, '//span[text()="Sign in"]').click()
    sleep(1)
    context.driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()

@then("Verify Sign In form opened")
def verify_sign_in_form_opened(context):
    sleep(2)
    actual_text = context.driver.find_element(By.XPATH, '//span[text()="Sign into your Target account"]').text
    context.driver.find_element(By.ID, "login")
    assert "Sign into your Target account" in actual_text, f"Error! -Sign into your Target account- not in {actual_text}"
    print("Test case passed.")
