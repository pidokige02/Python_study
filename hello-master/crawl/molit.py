from bs4 import BeautifulSoup
import requests
import json

url = "http://rt.molit.go.kr/new/gis/getGugunListAjax.do" #POST

params = {
    'menuGubun': 'A',
    'srhType': '',
    'gubunCode': 'LAND',
    'sidoCode': '11'
}

headers = {
    'Referer': 'http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

session = requests.session()
res = session.post(url, params=params, headers=headers)
print(res.headers)
print(session.headers)

# res = requests.post(url, params=params, headers=headers)
# print(res.headers)
# res = requests.post(url, params=params, headers=headers)
# print(res.headers)

# html = res.text
# print(html)
# jsonData = json.loads(html)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

# for gu in jsonData["jsonList"]:
#     print(gu['NAME'], gu['CODE'])
