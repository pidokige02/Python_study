# fname = '/Users/jade/Documents/리치안자산관리.csv'
fname = '리치안자산관리2.csv'

def cts(ct):
    ret = [0, 0, 0, 0]
    if '오전 9시~12시' in ct:
        ret[0] = 1
    
    if '오후 12시~3시' in ct:
        ret[1] = 1

    if '오후 3시~6시' in ct:
        ret[2] = 1

    if '오후 6시~9시' in ct:
        ret[3] = 1

    return ret

def proc(line):
    createdate, ct, addr, gender, name, mobile = line.split(',')
    # print(ct, gender, '=>', cts(ct), 1 if gender == '여성' else 0)
    sql = "insert into TlxEvent(cid, age, createdate, addr, female, name, mobile, consultime, consultime2, consultime3, consultime4) values(4, 1, '{}', '{}', {:d}, '{}', '{}', {}, {}, {}, {});"

    c = cts(ct)
    print(sql.format(createdate, addr, 1 if gender == '여성' else 0, name, mobile, c[0], c[1], c[2], c[3]))

with open(fname, 'r') as file:
    for line in file:
        # print(line.strip())
        proc(line.strip())
