import csv
import codecs
import random

fp = codecs.open("../exam/students.csv", "r", "utf-8")

# aaa,bbb,"ccc,cc"
reader = csv.reader(fp, delimiter=',', quotechar='"')

with codecs.open('./output.csv', 'w', 'utf-8') as ff:
    writer = csv.writer(ff, delimiter=',', quotechar='"')

    for cells in reader:
        writer.writerow([cells[0], random.randrange(1, 100) / 2])

    writer.writerow([ 'aaa', '24/7' ])
