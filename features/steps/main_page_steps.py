from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, "search")
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "div[data-test*='CartIcon']")
HEADER = (By.CSS_SELECTOR, "[class*='HeaderContainer']")
HEADER_LINKS = (By.CSS_SELECTOR, 'a[data-test*="GlobalHeader/UtilityHeader"]')



@given("Open target.com")
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)


@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(10)


@when("Click on Cart icon")
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(*HEADER)
    sleep(3)


@then('Verify header has {expected_amount} links')
def verify_header_has_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == expected_amount, f'Expected {expected_amount} links, but got {len(links)}'
    for link in links:
        print(link.text)


