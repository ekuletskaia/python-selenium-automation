from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, '//div[@data-test="resultsHeading"]')
    ADD_TO_CART_BTN1 = (By.CSS_SELECTOR, 'button[data-test="chooseOptionsButton"]')
    FAVORITES_BTN = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')
    FAVORITES_TOOLTIP_TEXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        fav_btn = self.find_elements(*self.FAVORITES_BTN)
        print(fav_btn)
        actions = ActionChains(self.driver)
        actions.move_to_element(fav_btn[0])
        actions.perform()

    def verify_fav_tooltip(self):
        self.verify_text('Click to sign in and save', *self.FAVORITES_TOOLTIP_TEXT)

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BTN1).click()

