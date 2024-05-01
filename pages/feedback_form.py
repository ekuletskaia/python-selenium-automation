from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class FeedbackForm(Page):
    HEADER_FB_FORM = (By.XPATH, '//strong[text()="Guest feedback"]')
    WEBSITE_FB = (By.XPATH, '//label[text()="Website feedback"]')

    def verify_fb_form_opened(self):
        self.verify_item_visible(*self.HEADER_FB_FORM)

    def click_website_feedback(self):
        self.wait_until_clickable_click(*self.WEBSITE_FB)
