from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, "[class*='HeaderContainer']")
HEADER_LINKS = (By.CSS_SELECTOR, 'a[data-test*="GlobalHeader/UtilityHeader"]')


@given("Open target.com")
def open_target(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('Click Feedback')
def click_feedback(context):
    context.app.main_page.scroll_to_bottom()
    context.app.main_page.click_feedback()


@when("Search for {item}")
def search_product(context, item):

    context.app.header.search_product(item)


@when("Click on Cart icon")
def click_on_cart_icon(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart_icon()


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_has_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == expected_amount, f'Expected {expected_amount} links, but got {len(links)}'
    for link in links:
        print(link.text)


