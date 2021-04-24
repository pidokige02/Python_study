import requests
from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

res = requests.get(url)

with open("kma.xml", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "html.parser")
title = soup.select('item title')
print(title)
# print(soup.select('body data'))

for d in soup.select('body data'):
    seq = d.attrs['seq']
    ws = d.select_one('ws').text
    wd = d.select_one('wdkor').text
    print(seq, ws, wd)
