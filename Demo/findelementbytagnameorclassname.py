from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element(By.CLASS_NAME,"inputtext _55r1 _6luy _9npi").send_keys("validPASS")
driver.find_element(By.TAG_NAME,"button").click()
