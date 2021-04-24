import pymysql

def get_mysql_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')

def get_count(conn, tbl):
    cur = conn.cursor()
    sql = "select count(*) from " + tbl

    cur.execute(sql)
    return cur.fetchone()
