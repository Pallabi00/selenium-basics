from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/pallabi/Downloads/chromedriver")
driver = webdriver.chrome(service=serv_obj)
driver.get("https://www.orangehrm.com/")
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Password")

else:
    print("login test failed")
driver.close()