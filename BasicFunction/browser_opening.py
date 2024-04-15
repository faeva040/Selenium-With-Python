# atfirst go to terminal and command
# pip3 install selenium
# pip install webdriver-manager
# exit

from selenium import webdriver

from selenium.webdriver.chrome.service import  Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://lips.group/')
driver.maximize_window()