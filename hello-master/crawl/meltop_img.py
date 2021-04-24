import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
from PIL import Image

url = "https://www.melon.com/chart/index.htm"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.get(url, headers=heads)
html = res.text

soup = BeautifulSoup(html, "html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
print(len(trs))
# print(trs[0])

def resize_image(imgFile, new_file):
    img2 = Image.open(imgFile)
    new_img = img2.resize((50, 50))
    new_img.save(new_file)

for i, tr in enumerate(trs):
    song_no = tr.attrs['data-song-no']
    title = tr.select_one('div.ellipsis.rank01 a').text
    src = tr.select_one('a.image_typeAll img').get('src')
    img = requests.get(src, headers=heads).content
    imgFile = './images/' + str(i+1) + '.jpg'
    print("writing newFile...", src)
    with open(imgFile, mode="wb") as file:
        file.write(img)

for i in range(100):
    imgFile = './images/' + str(i+1) + '.jpg'
    newFile = './images/' + str(i+1) + '_50x50.jpg'
    resize_image(imgFile, newFile)
        
