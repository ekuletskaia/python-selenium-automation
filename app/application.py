from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.add_to_cart_modul import AddToCartModul


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.add_to_cart_modul = AddToCartModul(driver)
