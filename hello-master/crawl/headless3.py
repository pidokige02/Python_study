import time
from selenium import webdriver
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
# or.   options.add_argument("--disable-gpu")
options.add_argument("disable-gpu")
# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver', options=options)

driver.implicitly_wait(3)

url = "https://www.skyscanner.net/transport/flights/sela/syda?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1902&selectedoday=01"
driver.get(url)
time.sleep(1)

# or.  driver.get_screenshot_as_file('bbb.png')
# driver.save_screenshot("bbb.png")
print(">>>>>>>", driver.title)
driver.implicitly_wait(5)
driver.quit()
