from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "div[data-test*='CartIcon']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart_icon(self):
        self.wait_until_clickable_click(*self.CART_ICON)