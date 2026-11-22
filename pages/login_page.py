from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".ico-logout")

    def open_login_page(self):
        self.click(self.LOGIN_LINK)

    def fill_email_field(self, email):
        self.fill(self.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def is_logout_displayed(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.LOGOUT_BUTTON
            )
        )
        return element.is_displayed()