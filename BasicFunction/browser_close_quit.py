from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.facebook.com')
#driver.maximize_window()
driver.fullscreen_window()

# close current open window
#driver.close()


# close all open window
#driver.quit()
