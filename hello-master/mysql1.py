import pymysql

conn = pymysql.connect(
    host='localhost',
    user='dooo',
    password='dooo!',
    port=3306,
    db='dooodb',
    charset='utf8')

with conn:
    cur = conn.cursor()
    sql = "select id, stu, cast(stu as char(3)), cast( cast(stu as char(3)) as decimal(3,2)) from dooodb.qqq"
    cur.execute(sql)
    rows = cur.fetchall()

for row in rows:
    print(row)
