from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests.base_test import BaseTest


class TestCheckout(BaseTest):

    def test_buy_one_product(self):
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        product_page.open_books_page()
        product_page.select_product()
        product_page.add_to_cart()

        cart_page.open_cart()



        cart_page.agree_to_terms()
        cart_page.proceed_to_checkout()

        checkout_page.fill_billing_address("andrey.qa.54@gmail.com")
        checkout_page.continue_billing()
        checkout_page.continue_shipping()
        checkout_page.continue_shipping_method()
        checkout_page.continue_payment_method()
        checkout_page.continue_payment_info()
        checkout_page.confirm_order()

        assert checkout_page.is_order_successful()