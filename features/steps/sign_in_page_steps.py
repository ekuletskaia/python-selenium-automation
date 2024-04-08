from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


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
