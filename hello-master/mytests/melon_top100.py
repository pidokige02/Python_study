from bs4 import BeautifulSoup
import requests
import json
import csv, codecs

url = "https://www.melon.com/chart/index.htm"
jsonUrl = "https://www.melon.com/commonlike/getSongLike.json"

selector = "span.cnt"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

dic = {}
for tr in soup.select('tr[data-song-no]'):
    song_no = tr.attrs['data-song-no']
    ranking = int(tr.select_one('span.rank').text)
    title = tr.select_one('div.ellipsis.rank01 a')
    singer = tr.select('div.ellipsis.rank01 a')
    singers = set( [ a.text for a in tr.select('div.ellipsis.rank02 a') ] )
    # print(singers)
    dic[song_no] = {"rank": ranking, "song_no": song_no, "title": title.text, "singer": ",".join(singers)}

# print(dic)

params = {
    "contsIds": ",".join(dic.keys())
}

# vals = [v['song_no'] for k, v in dic.items()]
# print(";".join(vals))

reqJson = requests.get(jsonUrl, headers=headers, params=params)
print(reqJson.url, reqJson.headers)
likeJsonStr = reqJson.text
jsonData = json.loads(likeJsonStr)

for j in jsonData['contsLike']:
    k = str(j['CONTSID'])
    dic[k]['likecnt'] = j['SUMMCNT']
    print(j)

# print(json.dumps(jsonData, ensure_ascii=False, indent=2))
print(dic)

# d[0]은 키, d[1]은 value json!!
# sort_dic = sorted(dic.items(), key=lambda d: d[1]['rank'], reverse=True)
# sort_dic = sorted(dic.items(), key=lambda d: d[0], reverse=True)
# sort_dic = sorted(dic.items(), reverse=True)  ## key로 sort!!
# sort_dic = sorted(dic, reverse=True)  ## key로 sort, 단, value가 없이 키만 담는다!!

import pprint
pprint.pprint(dic)

with codecs.open('./csv_melon.csv', 'w', 'utf-8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"')
    writer.writerow(['랭킹', '제목', '가수명', '좋아요수'])
    total = 0
    for k, v in sorted(dic.items(), key=lambda d: d[1]['rank']):
        writer.writerow([ v['rank'], v['title'], v['singer'], v['likecnt'] ])
        total = total + v['likecnt']

    writer.writerow(['계', '', '', total])