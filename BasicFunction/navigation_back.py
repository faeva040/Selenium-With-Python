from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# open facebook
driver.get('https://www.facebook.com')
driver.maximize_window()


# open google
driver.get('https://www.google.com/')


# back to facebook page link
driver.back()
driver.forward()

print("successfully move page")