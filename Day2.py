
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service ("/usr/local/bin/chromedriver")

driver =webdriver.Chrome(service=serv_obj)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
print(f"there are {len(sliders)} sliders on the home page")# total number of sliders on home page
links = driver.find_elements(By.TAG_NAME,'a')
print(f"There are {len(links)} links on the home page") #total number of links on home page
driver.find_element(By.CSS_SELECTOR,"input.search_query").send_keys('Casual dresses')#tag and class
driver.find_element(By.CSS_SELECTOR, "button[name=submit_search]").click() #tag and attribute
driver.find_element(By.CSS_SELECTOR, "a.login[href='http://www.automationpractice.pl/index.php?controller=my-account']").click() # tag, class and attribute
time.sleep(20)