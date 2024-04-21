from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, '//div[@data-test="resultsHeading"]')
    ADD_TO_CART_BTN1 = (By.CSS_SELECTOR, 'button[data-test="chooseOptionsButton"]')

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'

    def add_to_cart(self):
        self.find_element(*self.ADD_TO_CART_BTN1).click()

