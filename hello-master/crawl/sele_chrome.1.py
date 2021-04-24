import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = '/Users/jade/workspace/python/chromedriver'
driver = webdriver.Chrome(drvPath)

driver.get("https://www.daum.net")
time.sleep(2)

id = driver.find_element_by_id('id')
pw = driver.find_element_by_id('inputPwd')
pw.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()

