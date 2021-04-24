from bs4 import BeautifulSoup
import requests
from jputils.Game import Game

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')
# print(card_list)

print(">>>>>>>>>", type(card_list), type(card_list[0]))
games = []
for i in card_list:
    cards = i.select('div.card')
    print("LLL>>", len(cards))
    tmpi = 0
    for c in cards:
        games.append(Game(c))

with open("games.csv", "w", encoding='utf-8') as file:
    file.write("게임명\t제조사\t가격\t평점\n")
    for i in games:
        file.write(str(i) + "\n")


