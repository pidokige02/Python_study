import json

dic = {}

# html 파싱 데이터
for i in range(100):
    song_no = i + 1
    tempDic = {"CONTSID": song_no, "name": "name" + str(i + 1)}
    dic[song_no] = tempDic

# dic1 = {"songno": 2, "name": "bbb", "like": 0}

print(dic)
print("-------------------------------------")

# json data
strJson = '{"contsLike":[{"CONTSID":1,"LIKEYN":"N","SUMMCNT":11111},{"CONTSID":3,"LIKEYN":"N","SUMMCNT":70128},{"CONTSID":100,"LIKEYN":"N","SUMMCNT":100000},{"CONTSID":5,"LIKEYN":"N","SUMMCNT":22821},{"CONTSID":7,"LIKEYN":"N","SUMMCNT":70128},{"CONTSID":9,"LIKEYN":"N","SUMMCNT":63636}],"httpDomain":"http://www.melon.com","httpsDomain":"https://www.melon.com","staticDomain":"https://static.melon.co.kr"}'

jsonData = json.loads(strJson)
for j in jsonData['contsLike']:
    print("jjj=", j)
    k = j['CONTSID']
    print(dic[k])
    dic[k]['likecnt'] = j['SUMMCNT']
    print()

print("===============================")
print(dic)
