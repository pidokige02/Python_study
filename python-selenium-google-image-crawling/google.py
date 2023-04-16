from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q") # inspect한 element name 이 'q'임  
elem.send_keys("조코딩") # search keyword 조코딩이고 
elem.send_keys(Keys.RETURN) # enter key 를 누름.

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # 마지막까지 scroll 하였는가?
        try:
            driver.find_element_by_css_selector(".mye4qd").click()  # 결과 더보기 버튼 click
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")  # 모든 image 를 찾는다
count = 1
for image in images:
    try:
        image.click()  # 작은 image 를 click 하여 큰 image 로 만든다.
        time.sleep(2)  # image 를 click 한 후 기다리는 시간
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")  # 큰 image 의 url 은 얻어온다. 
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")  # count는 숫자이므로 문자열화 한다. 모든 image 를 jpg 로 각각 download 받는다.
        count = count + 1
    except:
        pass  # 오류가 나면 넘어가고 다움것을 처리하겠다.

driver.close()