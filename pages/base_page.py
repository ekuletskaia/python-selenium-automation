from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        f'Element {locator} not clickable').click()

    def verify_item_visible(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator),
                        f'Element is not visible - {locator}')

    def verify_item_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def verify_text(self, text, *locator):
        actual_text = self.find_element(*locator).text
        assert text == actual_text, f'Error! {text} not in {actual_text}'

    def verify_partial_text(self, text, *locator):
        actual_text = self.find_element(*locator).text
        assert text in actual_text, f'Error! {text} is not in {actual_text}'

    def url_contains(self, expected_text):
        self.wait.until(EC.url_contains(expected_text)), f'URL does not contain {expected_text}'

    def url_matches(self, expected_text):
        self.wait.until(EC.url_matches(expected_text)), f'URL does not match with {expected_text}'

