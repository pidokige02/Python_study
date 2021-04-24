import pymysql
import csv
import codecs

def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')

# sql_truncate = "truncate table Meltop"
sql_truncate = "delete from Meltop"
sql_insert = "insert into Meltop(rank, title, singer, likecnt) values(%s,%s,%s,%s)"
isStart = True

def save(lst):
    try:
        conn = get_conn('dadb')
        conn.autocommit = False
        cur = conn.cursor()

        global isStart
        if isStart:
            cur.execute(sql_truncate)
            isStart = False

        cur.executemany(sql_insert, lst)
        conn.commit()
        print("Affected RowCount is", cur.rowcount, "/", len(lst))

    except Exception as err:
        try:
            conn.rollback()
        except:
            print("Error on Rollback!!")
            
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")

        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)


csvFile = codecs.open("../crawl/data/meltop100.csv", "r", "utf-8")
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

total = len(list(reader))
print(total)

csvFile2 = codecs.open("../crawl/data/meltop100.csv", "r", "utf-8")
reader2= csv.reader(csvFile2, delimiter=',', quotechar='"')

lst = []
save_unit = 15
for i, row in enumerate(reader2):
    # if i != 0 and row[0] != '계':
    # print(i,total, row)
    if i != 0 and i != (total - 1):
        lst.append([row[0] , row[1], row[2], row[3]])

    if len(lst) == save_unit or i == (total - 1):
        save(lst)
        lst.clear()
