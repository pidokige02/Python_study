import bigquery
import pymysql
from collections import namedtuple
import sys
from pprint import pprint
client = bigquery.get_client(json_key_file='./bq.json', readonly=False)

DATABASE = "bqdb"
TABLE = "Song"
if not client.check_table(DATABASE, TABLE):
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'},
    ])


def pushFromMysql():
    conn = pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db='dadb',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

    with conn:
        cur = conn.cursor()
        cur.execute("select songno, title, albumid from Song limit 5")
        rows = cur.fetchall()

        # cols = [c[0] for c in cur.description]
        # print(cols, " ".join(cols))
        print(rows)

        # Song = namedtuple('Song', " ".join(cols))
        # dset = [Song(*r)._asdict() for r in rows]
        # pprint(dset)

        pushResult = client.push_rows(DATABASE, TABLE, rows, insert_id_key='songno')

        print("Pushed Result is", pushResult)


pushFromMysql()
