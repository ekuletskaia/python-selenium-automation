from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LISTINGS = (By.CSS_SELECTOR, 'div[data-test*="ProductCardWrapper"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'a[data-test="product-title"]')
PRODUCT_IMAGE = (By.CSS_SELECTOR, 'picture[data-test*="ProductCardImage"]')


@then("Verify search results are shown for {expected_item}")
def verify_search_results(context, expected_item):

    context.app.search_results_page.verify_search_results(expected_item)


@then('Verify URL has {expected_text}')
def verify_url_has_text(context, expected_text):

    context.app.base_page.url_contains(expected_text)


@when('Add product to Cart')
def add_to_cart(context):

    context.app.search_results_page.add_to_cart()
    context.app.add_to_cart_modul.add_product_to_cart()

    # context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN2),
    #                    message="Button Add to Cart not present on the page")
    # context.driver.find_element(*ADD_TO_CART_BTN2).click()
    # context.driver.find_element(*VIEW_CART_BTN).click()


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
