from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @then('Verify Guest feedback modul opened')
# def verify_fb_form_opened(context):
#     context.app.feedback_form.verify_fb_form_opened()

@when('Click Website feedback')
def click_website_feedback(context):
    context.app.feedback_form.click_website_feedback()