from bs4 import BeautifulSoup
import requests
import time
import urllib.parse as parse

url = "http://www.jobkorea.co.kr/Recruit/Home/_GI_List/"
# url = "http://www.jobkorea.co.kr/Recruit/Home/_GI_List/duty=1000100,1000101,1000102"

params = {
    'duty': ['1000100','1000101','1000102'],
    # 'duty': '1000100, 1000101, 1000102',
    # 'condition[duty]': ['1000100','1000101','1000102'],
    # 'condition[duty]': '1000100,1000101,1000102,1000096,1000097',
    # 'condition[duty]': '1000100,1000101,1000102,1000096,1000097',
    # 'condition': {
    #     'duty': ['1000100', '1000101', '1000102']
    # }
    # 'page': '1',
    # 'order': '2',
    # 'pagesize': '10',
    # 'condition[menucode]': [''],
    # 'direct': '0',
    # 'tabindex': '0',
    # 'fulltime': '0',
    # 'isDefault': 'true',
    # 'confirm': '0'
}

headers = {
    'Referer': 'http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

req = requests.post(url, params=params, headers=headers)
# req = requests.post(url, data=params, headers=headers)
print(req.url)

import urllib
print(urllib.parse.qu)
html = req.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')


sel_comptitle = "div.tplList div.titBx a"
sel_compname = "div.tplList td.tplCo "

get_url = soup.select(sel_comptitle)
get_name = soup.select(sel_compname)

# print(get_url)

company_name = []
url2 = []

b = 0
for i in get_url:
    a = i.get('href')
    url2.append("http://www.jobkorea.co.kr" + a)
    # print ("\n\n" , "http://www.jobkorea.co.kr" + a)


for j in get_name:
    c = j.select_one('a').text
    company_name.append(c)
    b += 1
    print(c, b)


name_url = []
# print (len(url2))
for i in range(len(url2)):
    name_url.append((company_name[i], url2[i]))


# print ("=====================\n\n\n\n" ,name_url)


data = soup.select("#dev-gi-list div.titBx a")
for i in data:
    href = i.get('href')
    # print(href)

# for k in url2:
#     function.request_url(k, '#gib_frame')
#     print(k, "\n\n")
#     time.sleep(3)
