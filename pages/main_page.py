from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    SIGN_IN_BTN = (By.XPATH, '//span[text()="Sign in"]')
    SIGN_OUT_BTN_FROM_SIDE_MENU = (By.XPATH, '//a[@data-test="accountNav-signIn"]')

    def open_main(self):
        self.driver.get("https://www.target.com/")

    def click_sign_in(self):
        self.driver.find_element(*self.SIGN_IN_BTN).click()
        self.driver.find_element(*self.SIGN_OUT_BTN_FROM_SIDE_MENU).click()