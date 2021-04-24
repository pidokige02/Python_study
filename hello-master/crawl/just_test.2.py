from bs4 import BeautifulSoup
import requests
import json

url = "https://www.skyscanner.net/transport/flights/sela/syda?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1902&selectedoday=01"

html = requests.get(url).text
print(html)


with open("./data/just_test2.html", mode="w") as file:
    file.write(html)

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

print(soup.select(".price"))
