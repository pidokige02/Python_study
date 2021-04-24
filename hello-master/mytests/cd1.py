import csv, codecs
import random

file = "../exam/students.csv"
fp = codecs.open(file, "r", "utf-8")

reader = csv.reader(fp, delimiter=',', quotechar='"')

with codecs.open('./output.csv', 'w', 'utf-8') as ff:
    writer = csv.writer(ff, delimiter=',', quotechar='"')
    for cells in reader:
        print(cells[0], cells[1])
        if cells[0] == '이름':
            writer.writerow([cells[0], '성적'])
        else:
            writer.writerow([cells[0], random.randrange(1,100)])
