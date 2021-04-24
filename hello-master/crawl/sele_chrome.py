import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')  # mac or linux

driver.get("https://www.google.com")
# time.sleep(2)


ctrl = Keys.CONTROL
if os.name == 'posix':
    ctrl = Keys.COMMAND

inputElement = driver.find_element_by_name("q")
inputElement.send_keys("세종대왕")
inputElement.send_keys(Keys.COMMAND, "a")
time.sleep(1)
inputElement.send_keys(ctrl, "c")
inputElement.send_keys(Keys.DELETE)
time.sleep(1)
inputElement.send_keys(ctrl, "v")
inputElement.send_keys("훈민정흠")

inputElement.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()
