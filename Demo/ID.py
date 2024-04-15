from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.facebook.com/')
driver.maximize_window()

#check for ID
driver.find_element(By.ID,"email").clear()
driver.find_element(By.ID,"email").send_keys("validuserid")


#check for password
driver.find_element(By.ID,"pass").clear()
driver.find_element(By.ID,"pass").send_keys("validpass")


#check for login
driver.find_element(By.NAME,"login").click()

driver.implicitly_wait(5)
driver.close()