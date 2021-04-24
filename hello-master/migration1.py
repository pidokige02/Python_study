import mig_util as mu

conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')

# read from source db
with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select id, name, prof, classroom from Subject"

    cur.execute(sql)
    rows = cur.fetchall()

# write to target db
with conn_dadb:
    cur = conn_dadb.cursor()
    # cur.execute('truncate table Subject')
    trc = mu.trunc_table(conn_dadb, 'Subject')
    print("tuncated>>", trc)

    sql = '''insert into Subject(id, name, prof, classroom)
                          values(%s, %s, %s, %s)'''
    cur.executemany(sql, rows)
    print("AffectedRowCount is", cur.rowcount)
    conn_dadb.commit()


