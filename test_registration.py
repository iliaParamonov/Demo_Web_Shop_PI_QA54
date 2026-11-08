import secrets
from uuid import uuid4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_registration():
    email = "Test1@yandex.com"
    password = "test1qwerty"

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        # Open registration page
        driver.get("https://demowebshop.tricentis.com/register")

        # Fill registration form
        wait.until(
            EC.visibility_of_element_located((By.ID, "FirstName"))
        ).send_keys("Test")

        driver.find_element(By.ID, "LastName").send_keys("User")
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(password)

        # Click Register
        driver.find_element(By.ID, "register-button").click()

        # Verify successful registration
        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".registration-result-page .result")
            )
        ).text.strip()

        print("Registration message:", success_message)

        assert success_message == "Your registration completed"

    finally:
        driver.quit()