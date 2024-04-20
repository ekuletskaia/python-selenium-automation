from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    TEXT_CART_EMPTY = By.XPATH, "//h1[text()='Your cart is empty']"

    def verify_cart_is_empty(self):
        actual_text = self.find_element(*self.TEXT_CART_EMPTY).text
        assert "Your cart is empty" in actual_text, f'Error! text "Your cart is empty" not in {actual_text}'