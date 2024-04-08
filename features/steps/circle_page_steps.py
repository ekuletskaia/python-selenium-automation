from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CIRCLE_LINKS = (By.CSS_SELECTOR, '[data-component-id="WEB-397697"] [data-test*="/CellsComponent/Link"]')


@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)


@then('Verify {expected_circle_elements} circle elements are shown')
def verify_circle_elements(context, expected_circle_elements):
    expected_circle_elements = int(expected_circle_elements)
    actual_elements = context.driver.find_elements(*CIRCLE_LINKS)
    assert len(actual_elements) == expected_circle_elements, f'Expected {expected_circle_elements} links, but got {len(actual_elements)}'