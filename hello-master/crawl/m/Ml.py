import requests
from bs4 import BeautifulSoup
import pymysql
import re

ListURL = "http://vlg.berryservice.net:8099/melon/list"
ListLikeJson = "http://vlg.berryservice.net:8099/melon/likejson"

AlbumURL = "http://vlg.berryservice.net:8099/melon/detail"
AlbumRateJson = "http://vlg.berryservice.net:8099/melon/albumratejson"
AlbumLikeJson = "http://vlg.berryservice.net:8099/melon/albumlikejson"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

NoPattern = re.compile("\'(.*)\'")

def getNo(str):
    return re.findall(NoPattern, str)[0]

def getSoup(url, headers={}, params={}):
    res = requests.get(url, headers=headers, params=params)
    print("res.url>>", res.url)
    return BeautifulSoup(res.text, "html.parser")

class Ml:
    dic = {}

    def ttt(self):
        soup = getSoup('http://vlg.berryservice.net:8099/melon/detail?albumId=10123639', HEADERS)
        sn = soup.select_one('div.song_name ')
        print(sn, sn.text)
        print("----------------", sn.next.next, sn.next.next.next.next)


    def __init__(self):
        soup = getSoup(ListURL, HEADERS)
        trs = soup.select('div#tb_list table tbody tr[data-song-no]')
        print(len(trs))

        for tr in trs:
            song_no = tr.attrs['data-song-no']
            ranking = tr.select_one('span.rank').text
            title = tr.select_one('div.ellipsis.rank01 a').text
            # singers = tr.select('div.ellipsis.rank02 a')
            singers = tr.select('div.ellipsis.rank02 span a')
            singer = ",".join([a.text for a in singers])
            # for a in singers:
            #     print(a.get('href'), getNo(a.get('href')))
            album = getNo(tr.select_one('div.wrap a.image_typeAll').get('href'))
            # print(album)

            self.dic[song_no] = {'ranking': int(
                ranking), 'title': title, 'singer': singer, 'album': album}
