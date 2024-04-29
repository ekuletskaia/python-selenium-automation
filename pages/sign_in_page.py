from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):

    TEXT_SIGN_IN = (By.XPATH, '//span[text()="Sign into your Target account"]')
    EMAIL_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_WITH_PSW_BTN = (By.ID, "login")
    TC_LINK = (By.CSS_SELECTOR, 'a[aria-label*="terms & conditions"]')
    ERROR_MSG = (By.CSS_SELECTOR, '[data-test*="AlertDisplay"]')

    def open_sign_in_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def verify_user_isnt_logged_in(self):
        self.verify_item_visible(*self.ERROR_MSG)

    def verify_sign_in_form_opened(self):
        actual_text = self.driver.find_element(*self.TEXT_SIGN_IN).text
        expected_text = 'Sign into your Target account'
        assert actual_text in expected_text, f'Error! Text {expected_text} not in {actual_text}'

    def enter_email_and_password(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_sign_in_with_password(self):
        self.wait_until_clickable_click(*self.SIGN_IN_WITH_PSW_BTN)

    def verify_user_is_logged_in(self):
        self.verify_item_disappear(*self.TEXT_SIGN_IN)

    # def open_sign_in_page(self):
    #     self.open('https://www.target.com/login')

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_page(self):
        self.url_contains('terms-conditions')

