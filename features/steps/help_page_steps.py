from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PAGE_TITLE = (By.CSS_SELECTOR, '.col-sm-12 .custom-h2')
SEARCH_FIELD = (By.ID, 'j_id0:j_id2:j_id32:name')
SEARCH_BTN = (By.CSS_SELECTOR, 'input[alt="search"]')
AREA_1_LEFT = (By.CSS_SELECTOR, '.col-lg-12 .box-column')
AREA_1_RIGHT = (By.CSS_SELECTOR, '.grid_6 .salesforceBox')
AREA_2 = (By.CSS_SELECTOR, '.grid_4')
TITLE_ALL_HELP_PAGES = (By.XPATH, '//h2[text()="Browse all Help pages"]')


@given('Open Help page for Returns')
def open_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


# @then('Verify Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
#
# @then('Verify current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_header()

@then('Verify {header} page opened')
def verify_help_page_header(context, header):
    context.app.help_page.verify_header(header)


@given('Open Help page')
def open_circle_page(context):
    context.driver.get('https://help.target.com/help')
    sleep(7)


@then("Title 'Target Help' is shown")
def find_target_help_title(context):
    context.driver.find_element(*PAGE_TITLE)


@then('Search field is shown')
def find_search_field(context):
    context.driver.find_element(*SEARCH_FIELD)


@then('Search button is shown')
def find_search_button(context):
    context.driver.find_element(*SEARCH_BTN)


@then('Section_1 with 7 elements is shown')
def find_section_1(context):
    context.driver.find_element(*AREA_1_LEFT)
    context.driver.find_element(*AREA_1_RIGHT)


@then('Section_2 with {expected_elements} elements (contact us and product recalls) is shown')
def find_section_2(context, expected_elements):
    expected_elements = int(expected_elements)
    actual_elements = context.driver.find_elements(*AREA_2)
    assert len(actual_elements) == expected_elements, f'Expected {expected_elements} elements, but got {len(actual_elements)}'


@then('Title "Browse all Help pages" is shown')
def find_title_all_help_pages(context):
    context.driver.find_element(*TITLE_ALL_HELP_PAGES)