from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_HEADER = (By.XPATH, '//div[@data-test="resultsHeading"]')
ADD_TO_CART_BTN1 = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor82394015')
ADD_TO_CART_BTN2 = (By.CSS_SELECTOR, 'button[data-test="shippingButton"]')
VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[href="/cart"]')
ITEMS_IN_CART = (By.CSS_SELECTOR, 'span[class*=CartSummary]')
LISTINGS = (By.CSS_SELECTOR, 'div[data-test*="ProductCardWrapper"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'a[data-test="product-title"]')
PRODUCT_IMAGE = (By.CSS_SELECTOR, 'picture[data-test*="ProductCardImage"]')


@then("Verify search results are shown for {expected_item}")
def verify_search_results(context, expected_item):
    # actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    # assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
    context.app.search_results_page.verify_search_results(expected_item)

@when('Add product to Cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN1).click()
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN2),
                       message="Button Add to Cart not present on the page")
    context.driver.find_element(*ADD_TO_CART_BTN2).click()
    context.driver.find_element(*VIEW_CART_BTN).click()


@then('Verify {item} is in the cart')
def verify_item(context, item):
    context.driver.find_element(*ITEMS_IN_CART)


@then('Verify search results display product name and product image')
def verify_search_results(context):

    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(8)
    # context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)[:4] # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMAGE)
