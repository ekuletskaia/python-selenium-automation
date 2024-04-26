from pages.base_page import Page
from selenium.webdriver.common.by import By


class TargetAppPage(Page):

    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']" )

    def open_target_app_page(self):
        self.open('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        self.click(*self.PP_LINK)

    def verify_pp_page(self):
        self.url_contains('target-privacy-policy/')
