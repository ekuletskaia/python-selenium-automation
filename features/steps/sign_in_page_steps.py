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
    context.app.sign_in_page.verify_user_is_logged_in()


# @given('Open sign in page')
# def open_sign_in_page(context):
#     context.app.sign_in_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_page_opened(context):
    context.app.sign_in_page.verify_tc_page()


@then('User can close new window and switch back to original')
def return_to_original_window(context):
    context.app.sign_in_page.switch_window_by_id(context.original_window)




