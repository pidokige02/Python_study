import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x2080')

options.add_argument("disable-gpu")         # or.   options.add_argument("--disable-gpu")

driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver', options=options)

driver.implicitly_wait(3)

driver.get("https://www.naver.com")
time.sleep(2)

driver.save_screenshot("bbb.png")
driver.get_screenshot_as_file('ccc.png')
driver.implicitly_wait(5)
driver.quit()
