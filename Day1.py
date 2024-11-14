import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Service and WebDriver
serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

# Navigate to the page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the 'username' input field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Enter username and password
username_field.send_keys("Admin")

# Wait for the password field to be present
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

password_field.send_keys("admin123")

# Wait for the login button to be clickable and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))
)
login_button.click()

# Verify the title of the page
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login passed")
else:
    print(f"Login failed, actual title: {act_title}")


time.sleep(20)

# Close the browser
driver.quit()
