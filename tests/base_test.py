import os
import pytest

from pages.login_page import LoginPage


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

        self.login_page.open_login_page()
        self.login_page.fill_email_field("andrey.qa.54@gmail.com")
        self.login_page.fill_password_field(os.environ["DEMO_PASSWORD"])
        self.login_page.click_login_button()

        assert self.login_page.is_logout_displayed()