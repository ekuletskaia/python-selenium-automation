from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    TEXT_CART_EMPTY = By.XPATH, "//h1[text()='Your cart is empty']"

    def verify_cart_empty_msg(self):
        self.verify_text('Your cart is empty', *self.TEXT_CART_EMPTY)