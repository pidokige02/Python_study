
dic = {}

# html 파싱 데이터
dic0 = {"id": 1, "name": "aaa", "like": 0}
dic1 = {"id": 2, "name": "bbb", "like": 0}

dic[dic0['name']] = dic0
dic[dic1['name']] = dic1

print(dic)

# 찾기
bbbJson = dic['bbb']

# 못찾을 경우 (키 존재여부 체크하기)
if 'ccc' in dic:          # 또는  if (dic.get('ccc')):
    bbbJson2 = dic['ccc']

# 수정 및 추가하기
bbbJson['like'] = 1
bbbJson.update({'others': 'pppppppp'})

print(dic['bbb'])
print(dic)
