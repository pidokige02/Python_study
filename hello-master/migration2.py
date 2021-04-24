import mig_util as mu

connection = mu.get_oracle_conn()
myconn = mu.get_mysql_conn('dadb')

with connection:
    # cursor를 만들어줍니다
    cursor = connection.cursor()

    sql = '''select region_id, region_name from Regions'''

    # cursor.execute(sql, dept_id=30)
    cursor.execute(sql)

    rows = cursor.fetchall()

for row in rows:
    print(row)

with myconn:
    cur = myconn.cursor()
    cur.execute("drop table if exists Regions")

    sql_create = '''
        create table Regions(
            id smallint not null auto_increment primary key,
            region_name varchar(36)
        )
    '''
    cur.execute(sql_create)

    sql_insert = "insert into Regions(id, region_name) values(%s, %s)"
    cur.executemany(sql_insert, rows)
    print("AffectedRowCount is", cur.rowcount)


