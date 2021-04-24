import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

UserId = "jeonseongho"
UserPw = "!mD:L76YQn.Bfa7"

options = webdriver.ChromeOptions()
# options.add_argument('headless')
#options.add_argument('window-size=1920x1080')

# options.add_argument("disable-gpu")
#options.add_argument("--disable-gpu")

# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# options.add_argument("lang=ko_KR")
# options.add_argument("Referer=https://naver.com")

driver = webdriver.Chrome(
    '/Users/jade/workspace/python/chromedriver', options=options)
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')

driver.implicitly_wait(3)


driver.get('https://naver.com')
driver.implicitly_wait(2)
driver.find_element_by_class_name('lg_local_btn').click()

# url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
# url = "https://nid.naver.com/nidlogin.login"
# driver.get(url)
print("open login page...")
time.sleep(1)

# driver.maximize_window()

eleId = driver.find_element_by_id('id')
eleId.clear()
eleId.send_keys(UserId)
elePw = driver.find_element_by_id('pw')
elePw.clear()
elePw.send_keys(UserPw)

btnLogin = driver.find_element_by_css_selector('input.btn_global').click()
print("click the login button...")


time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.close()
