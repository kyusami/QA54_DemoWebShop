from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    CART_LINK = (By.CSS_SELECTOR, ".ico-cart")
    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def open_cart(self):
        self.click(self.CART_LINK)

    def agree_to_terms(self):
        self.click(self.TERMS_CHECKBOX)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)