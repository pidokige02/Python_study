import time
from selenium import webdriver

# TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'
TEST_URL = "https://www.skyscanner.net/transport/flights/sela/syda?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1902&selectedoday=01"

options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('window-size=1920x1080')

options.add_argument("disable-gpu")
#options.add_argument("--disable-gpu")

options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver', options=options)

driver.implicitly_wait(3)

driver.get('about:blank')
driver.execute_script(
    "Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
driver.get(TEST_URL)
#time.sleep(2)

# user_agent = driver.find_element_by_css_selector('#user-agent').text
# plugins_length = driver.find_element_by_css_selector('#plugins-length').text

# print('User-Agent: ', user_agent)
# print('Plugin length: ', plugins_length)

driver.save_screenshot("bbb.png")
#driver.get_screenshot_as_file('bbb.png')
print(driver.title)

#driver.implicitly_wait(5)
driver.quit()
