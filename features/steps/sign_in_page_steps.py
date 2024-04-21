from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click Sign In")
def click_sign_in(context):

    context.app.main_page.click_sign_in()


@then("Verify Sign In form opened")
def verify_sign_in_form_opened(context):

    context.app.sign_in_page.verify_sign_in_form_opened()


@when('Enter valid {email} and {password}')
def enter_email_and_password(context, email, password):

    context.app.sign_in_page.enter_email_and_password(email, password)


@when('Click Sign in with password')
def click_sign_in_with_password(context):

    context.app.sign_in_page.click_sign_in_with_password()


@then('Verify user is logged in')
def verify_user_is_logged_in(context):

    context.app.sing_in_page.verify_user_is_logged_in()
