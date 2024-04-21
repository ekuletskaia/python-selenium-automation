from selenium.webdriver.common.by import By
from pages.base_page import Page


class AddToCartModul(Page):

    ADD_TO_CART_BTN2 = (By.CSS_SELECTOR, 'button[data-test="shippingButton"]')
    VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[href="/cart"]')

    def add_product_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN2).click(), "Button Add to Cart not present on the page"
        self.driver.find_element(*self.VIEW_CART_BTN).click()
