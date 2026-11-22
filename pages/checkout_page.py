from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    BILLING_CONTINUE = (By.CSS_SELECTOR, "#billing-buttons-container input")
    SHIPPING_CONTINUE = (By.CSS_SELECTOR, "#shipping-buttons-container input")
    SHIPPING_METHOD_CONTINUE = (By.CSS_SELECTOR, "#shipping-method-buttons-container input")
    PAYMENT_METHOD_CONTINUE = (By.CSS_SELECTOR, "#payment-method-buttons-container input")
    PAYMENT_INFO_CONTINUE = (By.CSS_SELECTOR, "#payment-info-buttons-container input")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, ".confirm-order-next-step-button")

    ORDER_SUCCESS = (By.CSS_SELECTOR, ".order-completed .title")

    FIRST_NAME = (By.ID, "BillingNewAddress_FirstName")
    LAST_NAME = (By.ID, "BillingNewAddress_LastName")
    EMAIL = (By.ID, "BillingNewAddress_Email")
    COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    CITY = (By.ID, "BillingNewAddress_City")
    ADDRESS = (By.ID, "BillingNewAddress_Address1")
    ZIP_CODE = (By.ID, "BillingNewAddress_ZipPostalCode")
    PHONE = (By.ID, "BillingNewAddress_PhoneNumber")
    def click_continue(self, locator):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        button.click()

    def continue_billing(self):
        self.click_continue(self.BILLING_CONTINUE)

    def continue_shipping(self):
        self.click_continue(self.SHIPPING_CONTINUE)

    def continue_shipping_method(self):
        self.click_continue(self.SHIPPING_METHOD_CONTINUE)

    def continue_payment_method(self):
        self.click_continue(self.PAYMENT_METHOD_CONTINUE)

    def continue_payment_info(self):
        self.click_continue(self.PAYMENT_INFO_CONTINUE)

    def confirm_order(self):
        self.click_continue(self.CONFIRM_BUTTON)

    def is_order_successful(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.ORDER_SUCCESS
            )
        )
        return "successfully processed" in element.text.lower()

    def fill_billing_address(self, email):
        self.fill(self.FIRST_NAME, "Andrey")
        self.fill(self.LAST_NAME, "Test")
        self.fill(self.EMAIL, email)

        Select(self.find(self.COUNTRY)).select_by_visible_text("Israel")

        self.fill(self.CITY, "Ashkelon")
        self.fill(self.ADDRESS, "Test Street 10")
        self.fill(self.ZIP_CODE, "7810000")
        self.fill(self.PHONE, "0501234567")