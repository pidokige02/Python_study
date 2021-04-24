from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/marketindex/"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

usd = soup.select_one(
    "#exchangeList > li:nth-of-type(1) > a.head.usd > div > span.value")

# print(usd, type(usd), float(usd))
print("usd=", usd, float(usd.string.replace(',', '')))

print(usd.prettify() )
