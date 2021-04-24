from bs4 import BeautifulSoup
import requests

url = "https://www.melon.com/chart/index.htm"

selector = "span.cnt"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

html = requests.get(url, headers=headers).text

print(html)

with open("./data/just_test.html", mode="w") as file:
    file.write(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

print(soup.select(selector))
