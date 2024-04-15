from selenium import webdriver
from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.get('https://www.facebook.com')
driver.maximize_window()

# for click
click_action=driver.find_element(By.TAG_NAME,"button")
click_action.click()

#for click and hold
click_action=driver.find_element(By.TAG_NAME,"button")
webdriver.ActionChains(driver).click_and_hold(click_action).perform()
