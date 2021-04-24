from google.cloud import bigquery as bq
import bigquery
import pymysql
from collections import namedtuple
import sys, os
from pprint import pprint

KeyFile = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
client = bigquery.get_client(json_key_file=KeyFile, readonly=False)

DATABASE = "bqdb"
TABLE = "SongAlbums"
Sql = '''
    select s.songno, s.title, s.genre, s.likecnt, s.albumid,
        a.title as album_title, a.genre as album_genre,
        a.likecnt as album_likecnt, cast(a.rate as char(10)) as album_rate 
    from Song s inner join Album a on s.albumid = a.albumid
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
                    {'name': 'album_likecnt', 'type': 'integer', 'description': 'album likecnt'},
                    {'name': 'album_rate', 'type': 'FLOAT', 'description': 'album like rate'}
                ]
            }
        ])

def getData():
    conn = pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db='dadb',
        # cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

    with conn:
        cur = conn.cursor()
        cur.execute(Sql)

        cols = [ c[0] for c in cur.description ]
        print(cols)
        albumIdx = cols.index('albumid')

        for row in cur.fetchall():
            d = {}
            a = {}
            for i, r in enumerate(row):
                if i < albumIdx:
                    d[ cols[i] ] = r 
                else:
                    a[cols[i]] = r

            d['album'] = a
            yield d


def pushData():
        pushResult = client.push_rows(DATABASE, TABLE, getData(), insert_id_key='songno')
        print("Pushed Result is", pushResult)


def readData():
    client = bq.Client()
    QUERY = 'SELECT * FROM `%s.%s` LIMIT 100' % (DATABASE, TABLE)
    print("-------------------------------------------- send query")

    query_job = client.query(QUERY)  # API request
    print("---------------------------------------- get result")
    rows = query_job.result()        # Waits for query to finish
    for row in rows:
        print(row)

createIfNotExists()
pushData()
readData()
