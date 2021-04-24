from google.cloud import bigquery as bq
import bigquery
import pymysql
from collections import namedtuple
import sys, os
from pprint import pprint

KeyFile = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
client = bigquery.get_client(json_key_file=KeyFile, readonly=False)

DATABASE = "bqdb"
TABLE = "Song"
Sql = '''
    select s.songno, s.title, s.genre, s.likecnt, s.albumid,
        a.title as album_title, a.genre as album_genre,
        a.likecnt as album_likecnt, cast(a.rate as char(5)) as album_rate 
    from Song s inner join Album a on s.albumid = a.albumid
    order by s.songno
    limit 100
'''

def createIfNotExists():
    if not client.check_table(DATABASE, TABLE):
        print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

        client.create_table(DATABASE, TABLE, [
            {'name': 'songno', 'type': 'string', 'description': 'song id'},
            {'name': 'title', 'type': 'string', 'description': 'song title'},
            {'name': 'genre', 'type': 'string', 'description': 'genre'},
            {'name': 'likecnt', 'type': 'integer', 'description': 'song like count'},
            {'name': 'album', 'type': 'RECORD', 'description': 'album information', 
                'fields': [
                    {'name': 'albumid', 'type': 'string', 'description': 'album id'},
                    {'name': 'album_title', 'type': 'string', 'description': 'album title'},
                    {'name': 'album_genre', 'type': 'string', 'description': 'album title'},
                    {'name': 'album_likecnt', 'type': 'string', 'description': 'album likecnt'},
                    {'name': 'album_rate', 'type': 'FLOAT', 'description': 'album like rate'}
                ]
            }
        ] )

def getData():
    conn = pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db='dadb',
        # cursorclass=pymysql.cursors.DictCursor,  # 변환없이 바로 넣을때 사용!!
        charset='utf8')

    with conn:
        cur = conn.cursor()
        cur.execute(Sql)
        rows = cur.fetchall()

        cols = [ c[0] for c in cur.description ]
        album_idx = cols.index('albumid')
        print("-------------------------------")
        for row in rows:
            d = {}
            a = {}
            for i, r in enumerate(row):
                # print(cols[i], i, r)
                if i < album_idx:
                    d[cols[i]] = r
                else:
                    a[cols[i]] = r
            d['album'] = a
            yield d


        # Song = namedtuple('Song', " ".join(cols))
        # dset = [Song(*r)._asdict() for r in rows]
        # pprint(dset)

    # return rows

def read():
    readSql = "SELECT * FROM `bqdb.Song` LIMIT 100"
    query_job = bq.Client().query(readSql)  # API request
    rows = query_job.result()        # Waits for query to finish
    for row in rows:
        print(row)


createIfNotExists()
# ttt = getData()
# for t in ttt:
#     print("tttttttttt>>", t)
# exit()
# pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
pushResult = client.push_rows(DATABASE, TABLE, getData(), insert_id_key='songno')
print("Push Result is", pushResult)

read()

# rrr = getData()
# # print(type(rrr), len(rrr))
# for r in enumerate(rrr):
#     pprint(r)
