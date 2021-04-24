import sqlite3
from Student import Student

params = []
with open('students.csv', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        stu = Student(line)
        t = stu.make_params()
        # print(type(t), list(t))
        params.append(t)

# print(params)

conn = sqlite3.connect("exam.db")

def insert_data():
    with conn:
        cur = conn.cursor()
        sql = "insert into Student(name, gender, age, grade, addr) values(?,?,?,?,?)"
        cur.executemany(sql, params)

        conn.commit()

def select_data():
   with conn:
        cur = conn.cursor()
        # sql = "select id, name, gender, age, grade, addr from Student order by grade"
        sql = """select id, name, gender, age, grade, addr
                   from Student order by substr(grade,1,1), grade desc"""
        # print(sql)
        cur.execute(sql)
        rows = cur.fetchall();
        for row in rows:
            print(row)

insert_data()
select_data()
