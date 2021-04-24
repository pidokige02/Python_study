from bs4 import BeautifulSoup
import requests

url = "https://image-comic.pstatic.net/webtoon/721457/9/20190107143230_15d34308650589a5dbb7a30910dab27d_IMAG01_1.jpg"

headers = {
    "Referer": "https://comic.naver.com/webtoon/detail.nhn?titleId=721457&no=9&weekday=wed"
}
img = requests.get(url, headers=headers).content

saveFile = "./ttt/cc.png"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")
