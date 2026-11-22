from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    BOOKS_LINK = (By.LINK_TEXT, "Books")
    PRODUCT_LINK = (By.LINK_TEXT, "Computing and Internet")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart-button")

    def open_books_page(self):
        self.click(self.BOOKS_LINK)

    def select_product(self):
        self.click(self.PRODUCT_LINK)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)