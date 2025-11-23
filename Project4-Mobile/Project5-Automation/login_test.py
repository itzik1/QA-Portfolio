from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Basic configuration
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # 1. Open login page
    driver.get("https://example.com/login")

    # 2. Find email and password fields
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    # 3. Enter credentials
    email_input.send_keys("test@test.com")
    password_input.send_keys("123456")

    # 4. Click login button
    login_button = driver.find_element(By.ID, "login_button")
    login_button.click()

    # 5. Wait for page to load (simple demo)
    time.sleep(3)

    # 6. Basic assertion – check if "Dashboard" appears
    assert "Dashboard" in driver.page_source, "Dashboard was not loaded after login."

    print("Test passed: Login flow works as expected.")

finally:
    driver.quit()
