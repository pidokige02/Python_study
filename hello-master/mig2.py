import cx_Oracle

import os
print("----------------------------------------------")
print(os.environ['OCI_LIB'])
print("----------------------------------------------")
# os.setenv("ORACLE_HOME"="/usr/lib/oracle/12.1/client64")
# os.getenv("LD_LIBRARY_PATH")

# connection = cx_Oracle.connect("hr/hrpw@localhost/xe")
connection = cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
print(connection.version)

with connection:
    # cursor를 만들어줍니다
    cursor = connection.cursor()

    # sql = '''select * from Departments where department_id >= :dept_id'''
    sql = "select * from Employees where employee_id=157"

    # cursor.execute(sql, dept_id=30)
    # cursor.execute(sql, (30,))
    cursor.execute(sql)

    rows = cursor.fetchone()

for row in rows:
    print(row)


select COMMISSION_PCT, cast(COMMISSION_PCT as number(8, 10)) from Employees where employee_id = 157;
select lengthb(COMMISSION_PCT) from Employees where employee_id = 157;
