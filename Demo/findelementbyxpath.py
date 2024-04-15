import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.facebook.com/')
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("validusername")
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("validpass")
driver.find_element(By.XPATH,"//button[@id='u_0_9_qI']").click()

time.sleep(2)