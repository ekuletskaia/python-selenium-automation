from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    # use[href*="Account"]
    SIGN_IN_BTN = (By.CSS_SELECTOR, 'a[data-test = "@web/AccountLink"]')
    SIGN_OUT_BTN_FROM_SIDE_MENU = (By.XPATH, '//a[@data-test="accountNav-signIn"]')

    def open_main(self):
        self.driver.get("https://www.target.com/")

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN_BTN)
        self.wait_until_clickable_click(*self.SIGN_OUT_BTN_FROM_SIDE_MENU)