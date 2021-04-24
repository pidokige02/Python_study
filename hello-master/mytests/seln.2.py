import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

UserId = "jeonseongho"
UserPw = "!mD:L76YQn.Bfa7"

driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')

driver.implicitly_wait(3)


driver.get('https://naver.com')
driver.implicitly_wait(2)
driver.find_element_by_class_name('lg_local_btn').click()

print("open login page...")
time.sleep(1)

eleId = driver.find_element_by_id('id')
elePw = driver.find_element_by_id('pw')

# ActionChains(driver).move_to_element(eleId).click().key_down('j').key_down('e').key_down('o').key_down('n').perform()
# time.sleep(2)
# ActionChains(driver).move_to_element(eleId).click().key_down('s').key_down('e').key_down('o').key_down('n').perform()

eleId.send_keys('jeonseon')
# eleId.send_keys(Keys.BACK_SPACE)
elePw.send_keys('h')


# actions = ActionChains(driver)

# actions.move_to_element(eleId)
# actions.click(eleId)

# actions.send_keys_to_element(eleId, 'j')
# actions.send_keys_to_element(eleId, 'e')
# actions.send_keys_to_element(eleId, 'o')
# actions.send_keys_to_element(eleId, 'n')
# actions.send_keys_to_element(eleId, 's')
# actions.send_keys_to_element(eleId, 'e')
# actions.send_keys_to_element(eleId, 'o')
# actions.send_keys_to_element(eleId, 'n')
# actions.send_keys_to_element(eleId, 'g')
# actions.send_keys_to_element(eleId, 'h')
# actions.send_keys_to_element(eleId, 'o')
# for i in UserId:
#     actions.pause(1)
#     actions.send_keys_to_element(eleId, i) 
#     # actions.key_down(i)

# actions.perform()

aaa = False
if aaa:
    for i in UserId:
        actions.pause(0.1)
        actions.key_down(i)

    actions.key_down(Keys.TAB)

aaa = False
if aaa:
    for i in UserPw:
        print("pw>>", i)
        actions.pause(0.1)
        actions.key_down(i)

    actions.key_down(Keys.RETURN)
    actions.perform()

    time.sleep(1)
    driver.back()
    time.sleep(1)

    actions = ActionChains(driver)
    eleId = driver.find_element_by_id('id')
    actions.move_to_element(eleId)
    actions.click(eleId)

    for i in UserId:
        actions.key_down(i)

    actions.key_down(Keys.TAB)
    actions.perform()

# eleId.click()
# eleId.clear()
# print("::>>", random.randrange(1, 10) / 10)
# for i in UserId:
#     time.sleep(random.randrange(1, 10) / 10)
#     eleId.send_keys(i)

time.sleep(20)

# rr = random.randrange(1,5)
# print("sleeep>>", rr)
# eleId.send_keys(Keys.TAB)

# time.sleep(rr)

# elePw = driver.find_element_by_id('pw')
# # elePw.clear()
# for i in UserPw:
#     time.sleep(0.1)
#     elePw.send_keys(i)

# time.sleep(1)
# elePw.send_keys(Keys.RETURN)
# time.sleep(3)

# driver.back()
# print("back!!")
# time.sleep(1)

# driver.find_element_by_css_selector('input.btn_global').click()
# driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
# elePw.send_keys(Keys.RETURN)
print("click the login button...")


# time.sleep(5)                # cf.  driver.implicitly_wait(5)
# driver.close()
