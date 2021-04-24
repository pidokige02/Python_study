import cx_Oracle

connection = cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
print(connection.version)

with connection:
    # cursor를 만들어줍니다
    cursor = connection.cursor()

    sql = '''select hire_date, to_date(to_char(hire_date, 'YYYY-MM-DD'), 'YYYY-MM-DD') from Employees'''

    cursor.execute(sql)

    rows = cursor.fetchall()

for row in rows:
    print(row)
