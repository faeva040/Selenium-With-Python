from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.yatra.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
