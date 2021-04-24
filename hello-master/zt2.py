import mig_util as mu

# conn_dooodb = mu.get_mysql_conn('dooodb')
conn_dadb = mu.get_mysql_conn('dadb')

# read from source db
with conn_dadb:
    cur = conn_dadb.cursor()
    sql = '''
        select constraint_name, table_name from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
         where CONSTRAINT_SCHEMA = database() and REFERENCED_TABLE_NAME = 'Department'
    '''
    cur.execute(sql)
    rows = cur.fetchall()

    sql = "call sp_drop_foreign_key('Department')"
    cur.execute(sql)
    rows = cur.fetchall()

for row in rows:
    print(row)
