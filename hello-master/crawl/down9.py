#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

url = "https://image-comic.pstatic.net/webtoon/695796/86/20181214131148_fb44d76ace3208a8f0b492e56d03a1ed_IMAG01_1.jpg"

headers = {
    "referer": "https://comic.naver.com/webtoon/detail.nhn?titleId=695796&no=86&weekday=sun"
}

saveFile = "./images/comic_test.jpg"
mem = requests.get(url, headers=headers).content
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")
