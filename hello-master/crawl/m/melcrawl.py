from pprint import pprint
from Ml import Ml

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        # cursorclass=pymysql.cursors.DictCursor,
        # cursorclass=pymysql.cursors.SSCursor,
        charset='utf8')



ml = Ml()
dic = ml.dic

# pprint(dic)

for song in dic.values():
    print(song)

ml.ttt()

exit()

sql = "select name from Club where name=%(name)s or id = %(id)s"

conn = get_conn('dooodb')
with conn:
    cur = conn.cursor()
    cur.execute(sql, {'id':5, 'name':'요트부'})
    rows = cur.fetchall()
    print(rows)
    lst = [r[0] for r in rows]
    print(lst)
    if '테니스부' in lst:
        print( "999999999999999")
