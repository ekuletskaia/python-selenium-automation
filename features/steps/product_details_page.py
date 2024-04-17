from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, 'a[rel="nofollow"]')
SELECTED_COLOR = (By.XPATH, '//div[contains(@class, "styles__StyledHeaderWrapperDiv")]')


@given("Open target product {product_id} page")
def step_impl(context, product_id):
    context.driver.get(f"http://target.com/p/{product_id}")
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ["Black", "Blue", "Orange"]
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors}, did not match actual {actual_colors}'



