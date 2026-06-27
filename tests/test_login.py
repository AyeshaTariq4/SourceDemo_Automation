from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Launch Browser
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.get("https://www.saucedemo.com")

# Create Objects
login = LoginPage(driver)
inventory = InventoryPage(driver)
checkout = CheckoutPage(driver)

# Login
login.login("standard_user", "secret_sauce")
time.sleep(2)

# Add Product
inventory.add_product_to_cart()
time.sleep(2)

# Open Cart
inventory.open_cart()
time.sleep(2)

# Checkout
checkout.checkout()
time.sleep(2)

# Customer Details
checkout.customer_details("Ayesha", "Tariq", "52250")
time.sleep(2)

# Continue
checkout.continue_checkout()
time.sleep(2)

# Finish
checkout.finish_order()
time.sleep(3)

print("Project Executed Successfully!")

#input("Press Enter to Close Browser...")

driver.quit()