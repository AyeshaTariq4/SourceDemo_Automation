from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def customer_details(self, first, last, postal):
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first)

        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)

    def continue_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    def finish_order(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()