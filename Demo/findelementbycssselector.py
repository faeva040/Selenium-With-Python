from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,"#email").send_keys("ValidName")
driver.find_element(By.CSS_SELECTOR,"#pass").send_keys("ValidPass")
driver.find_element(By.CSS_SELECTOR,"#u_0_9_tK").click()



