import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class TestLogin:

    def test_successful_login(self, driver):
        driver.find_element(By.LINK_TEXT, "Log in").click()
        email = driver.find_element(By.ID, "Email")
        email.send_keys("andrey.qa.54@gmail.com")
        password = driver.find_element(By.ID, "Password")
        password.send_keys(os.environ["DEMO_PASSWORD"])
        driver.find_element(By.CSS_SELECTOR, "input.login-button").click()
        logout_button = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, ".ico-logout"))
        )

        assert logout_button.is_displayed()