from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    CART_ICON = (By.CSS_SELECTOR, "div[data-test*='CartIcon']")

    def open_main(self):
        self.driver.get("https://www.target.com/")

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()