from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# for facebook
driver.get('https://www.facebook.com/')
driver.maximize_window()

# for double click
click_action = driver.find_element(By.TAG_NAME,"button")
webdriver.ActionChains(driver).double_click(on_element=click_action).perform()

