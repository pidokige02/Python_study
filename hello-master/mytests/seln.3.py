import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

UserId = "colin0171"
UserPw = "KuczPmm7gYK3D2W"

driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')
driver.maximize_window()

driver.implicitly_wait(3)

driver.get('https://www.daum.net')
# driver.get('https://logins.daum.net/accounts/toploginform.do')
driver.implicitly_wait(2)

driver.switch_to.frame(driver.find_element_by_id('loginForm'))

eleId = driver.find_element_by_id('id')
elePw = driver.find_element_by_id('inputPwd')

eleId.send_keys(UserId)
elePw.send_keys(UserPw)
elePw.send_keys(Keys.RETURN)

print("click the login button...")


time.sleep(5)                # cf.  driver.implicitly_wait(5)
# driver.close()
