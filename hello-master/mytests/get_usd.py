from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

usd = soup.select_one("#exchangeList > li:nth-of-type(1) > a.head.usd > div > span.value").text
print("usd=", usd, float(usd.replace(',', '')))