import mig_util as mu

conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')
table = 'Subject'

def read_list(conn, sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchall()

# read from source db
with conn_dooodb:
    dooo_cnt = mu.get_count(conn_dooodb, table)
    dooo_list = read_list(
        conn_dooodb, "select id, name, prof, classroom, classroom cr2 from Subject order by rand() limit %s", round(dooo_cnt / 2,))

print(dooo_list)

# lst = []
# for row in dooo_list:
#     l = list(row)
#     l.append(l[3])
#     lst.append(l)

with conn_dadb:
    da_cnt = mu.get_count(conn_dadb, table)
    cur = conn_dadb.cursor()
    # sql = '''select * from Subject
    #           where id = %s and name = %s and prof = %s
    #             and (classroom = %s or classroom is null)'''
    sql = '''select * from Subject
              where id = %s and name = %s and prof = %s
                and (case when %s is null then classroom is null else classroom = %s end)'''

    # cur.executemany(sql, lst)
    cur.executemany(sql, dooo_list)
    print(cur.fetchmany(), cur.rowcount)
    # print(cur.fetchall(), cur.rowcount)
    # for row in dooo_list:
    #     cur.execute("select * from Subject where id = %s and name = %s and prof = %s and classroom = %s", row)
    #     print(row, "<=>", cur.fetchone())

print("dooodb =", dooo_cnt, ", dadb =", da_cnt)
if dooo_cnt == da_cnt:
    print("OK")

else:
    print("Not Valid Count!! dooodb =", dooo_cnt, ", dadb =", da_cnt)
