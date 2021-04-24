import requests, json
from bs4 import BeautifulSoup

headers = {
    "X-Naver-Client-Id": "dRgjJjP4QdJyV3qR8oqS",
    "X-Naver-Client-Secret": "uB4v_zPuG0"
}

params = {
    "display": 100,
    "start": 1,
    "sort": "date",
    "query": "파이썬"
}

# url = "https://openapi.naver.com/v1/search/book.json"
url = "https://openapi.naver.com/v1/search/blog"
# url = "https://openapi.naver.com/v1/search/image"
html = requests.get(url, params=params, headers=headers).text
jsonData = json.loads(html)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))
print(len(jsonData['items']))

for i in jsonData['items']:
    print(i['title'], i['link'], i['bloggername'], i['postdate'])
