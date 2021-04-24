import requests
from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

res = requests.get(url)
print(res.url)

with open("kma.xml", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "html.parser")

title = soup.select('item title')
print(title)
