import requests
from bs4 import BeautifulSoup
import pymysql
import json
import re
import pprint

Top100URL = "http://vlg.berryservice.net:8099/melon/list"
Top100LikeJson = "http://vlg.berryservice.net:8099/melon/likejson"
AlbumURL = "http://vlg.berryservice.net:8099/melon/detail"
AlbumLikeJson = "http://vlg.berryservice.net:8099/melon/albumlikejson"
AlbumRateJson = "http://vlg.berryservice.net:8099/melon/albumratejson"
SongUrl = "http://vlg.berryservice.net:8099/melon/songdetail"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

SqlAlbum = '''
    insert into Album(albumid, title, createdt, 
                                company, genre, likecnt, rate, crawldt)
                values( %(albumid)s, %(title)s, %(createdt)s, 
                        %(company)s, %(genre)s, %(likecnt)s, %(rate)s, date_format(now(), '%%Y-%%m-%%d') )
        on duplicate key update likecnt = %(likecnt)s, rate = %(rate)s
    '''
SqlSong = '''
    insert into Song(songno, title, genre, 
                                albumid, likecnt)
                values( %(songno)s, %(title)s, %(genre)s, 
                        %(albumid)s, %(likecnt)s )
        on duplicate key update likecnt = %(likecnt);
    '''
SqlSongRank = '''
    insert ignore into SongRank(rankdt, rank, songno) 
                values( date_format(now(), '%%Y-%%m-%%d'), %(rank)s, %(songno)s ) 
'''
SqlArtist = '''
    insert ignore into Artist(artistid, name, atype) 
                values( %(artistid)s, %(name)s, %(atype)s ) 
'''
SqlSongArtist = '''
    insert ignore into SongArtist(songno, artistid, atype) 
                values( %(songno)s, %(artistid)s, %(atype)s ) 
'''

SqlAllSongs = 'select songno from Song'

NoPattern = re.compile("\'(.*)\'")
NoPattern2 = re.compile("\((.*)\)")

def getNo(str, pattern=NoPattern):
    ret = ''
    fs = re.findall(pattern, str)
    if fs != None and len(fs) > 0:
        ret = fs[0]

    return ret

def get_conn():
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db='dooodb',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

def getHtml(url, params={}, headers=HEADERS):
    res = requests.get(url, headers=headers, params=params)
    print("getSoup.res>>", res.url)
    return res.text

def getSoup(url, params={}, headers=HEADERS):
    html = getHtml(url, params, headers)
    return BeautifulSoup(html, 'html.parser')

class Melon:
    songs = {}
    albums = []
    artists = []
    artistsDic = {}

    def getSongnoes(self):
        conn = get_conn()
        with conn:
            cur = conn.cursor()
            cur.execute(SqlAllSongs)
            return cur.fetchall()

    def __init__(self):
        oldsongs = self.getSongnoes()
        self.oldsongs = [os['songno'] for os in oldsongs]

        soup = getSoup(Top100URL)
        trs = soup.select('div#tb_list table tbody tr[data-song-no]')
        for i, tr in enumerate(trs):
            song_no = tr.attrs['data-song-no']
            ranking = tr.select_one('span.rank').text
            title = tr.select_one('div.ellipsis.rank01 a').text
            singers = tr.select('div.ellipsis.rank02 span a')
            albumid = tr.select_one('div.wrap a.image_typeAll').get('href')
            song_artists = []
            song_artists_types = []
            for a in singers: # 가수 셋팅!! 0:singer, 1:작사가, 2:작곡가, 3:편곡
                if song_no in self.oldsongs: continue

                artistid = getNo(a.get('href'))
                song_artists.append(artistid)
                song_artists_types.append(0)
                singer = {'name': a.text, 'artistid': artistid, 'atype': 0}
                self.artists.append(singer)

            self.songs[song_no] = {
                    'songno': song_no,
                    'rank': int(ranking), 
                    'title': title, 
                    'albumid': getNo(albumid),
                    'artists': song_artists,
                    'atypes': song_artists_types,
                    'likecnt': 0
                }

            # QQQ
            # if i > 1: break

    def setLikecnt(self):
        likeParams = {
            "contsIds": ",".join(self.songs.keys())
        }

        jsonData = json.loads(getHtml(Top100LikeJson, likeParams))
        for j in jsonData['contsLike']:
            key = str(j['CONTSID'])
            songno = self.songs.get(key)
            if songno == None:
                print(">>>>>", key, songno)
            else:
                songDic = self.songs[key]
                songDic['likecnt'] = j['SUMMCNT']

    def setAlbumData(self):
        for song in self.songs.values():
            albumid = song['albumid']
            album_params = {
                "albumId": albumid
            }
            soup = getSoup(AlbumURL, album_params)
            ainfo = soup.select_one('div#conts div.section_info div.entry')
            dl = ainfo.select_one('div.meta dl.list')
            album = {
                     'albumid': albumid,
                     'title': ainfo.select_one('div.song_name').next.next.next.next.strip(),
                     'createdt': dl.select_one('dd:nth-of-type(1)').text,
                     'genre': dl.select_one('dd:nth-of-type(2)').text,
                     'company': dl.select_one('dd:nth-of-type(4)').text,
                     }

            rateJson = json.loads(getHtml(AlbumRateJson, album_params))
            likeJson = json.loads(getHtml(AlbumLikeJson, album_params))
            album['rate'] = round(float(rateJson['infoGrade']['TOTAVRGSCORE']), 2)
            album['likecnt'] = likeJson['contsLike'][0]['SUMMCNT']

            self.albums.append(album)

    # 노래의 장르, 작사가, 작곡가
    def setSongOthers(self):
        for songno, song in self.songs.items():

            if songno in self.oldsongs:
                song['genre'] = ''
                continue

            params = {
                "songId": songno
            }

            soup = getSoup(SongUrl, params)
            conts = soup.select_one('div#conts')

            sinfo1 = conts.select_one('div.meta dl.list')
            genre = sinfo1.select_one('dd:nth-of-type(3)').text
            song['genre'] = genre
            

            arts = conts.select('ul.list_person.clfix li div.entry')
            for art in arts:
                # print(art)
                a = art.select_one('a')
                aname = a.text
                aid = getNo(a.get('href'), NoPattern2)
                atype = art.select_one('span').text
                atypeNo = self.getArtistType(atype)
                dicArtists = {'name': aname, 'artistid': aid,
                              'atype': atypeNo}
                self.artists.append(dicArtists)
                self.artistsDic[aid] = dicArtists
                # print(song['artists'], type(song['artists']))
                song['artists'].append(aid)
                song['atypes'].append(atypeNo)

    # 1:작사가, 2:작곡가, 3:편곡
    def getArtistType(self, atype):
        if atype == '작사':
            return 1
        elif atype == '작곡':
            return 2
        else:
            return 3

    def executeMany(self, sql, lst):
        conn = get_conn()
        with conn:
            cur = conn.cursor()
            cur.executemany(sql, lst)
            conn.commit()


    def saveAlbum(self):
        print(SqlAlbum, self.albums)
        self.executeMany(SqlAlbum, self.albums)

    def saveSong(self):
        self.executeMany(SqlSong, self.songs.values())

    def saveSongRank(self):
        self.executeMany(SqlSongRank, list(self.songs.values()))

    def saveArtists(self):
        self.executeMany(SqlArtist, self.artists)

    def saveSongArtists(self):
        # print(self.artists)
        lst = []
        for songno, song in self.songs.items():
            # print(song)
            artists = song['artists']
            atypes = song['atypes']
            for i, a in enumerate(artists):
                lst.append({'songno': songno, 'artistid': a, 'atype': atypes[i]})

        # print(lst)
        self.executeMany(SqlSongArtist, lst)




