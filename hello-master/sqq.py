import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

# x = random.choices(first_names, k = 2)
# print(x, type(x))
y = random.sample(first_names, 2)
print(y, type(y), ''.join(y))

def make_name():
    sung = random.choice(fam_names)
    name = random.sample(first_names, 2)
    return sung, name

conn = sqlite3.connect("t.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"

    p = ('김일수',)
    print(type(p))
    # cur.execute(sql, ['김일수'])
    cur.execute(sql, p)

    conn.commit()
