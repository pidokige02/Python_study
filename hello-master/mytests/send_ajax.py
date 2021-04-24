import requests, json

url = "http://rt.molit.go.kr/new/gis/getDanjiComboAjax.do"

params = {
    'menuGubun': 'A',
    'srhType': '',
    'srhYear': '2019',
    'srhLastYear': '2018',
    'gubunCode': 'LAND',
    'sidoCode': '11',
    'gugunCode': '11320',   #구
    'danjiName': '',
    'roadCode': '',
    'roadBun1': '',
    'roadBun2': '',
    'dongCode': '1132010800',  # 동
    'rentAmtType': '3'
}
# prm = "menuGubun=A&srhType=&srhYear=2019&srhLastYear=2018&gubunCode=LAND&sidoCode=11&gugunCode=11350&danjiName=&roadCode=&roadBun1=&roadBun2=&dongCode=1135010600&rentAmtType=3"

headers = {
    # 'Content-type': 'application/json; charset=UTF-8',
    # "Content-Type": "application/x-www-form-urlencoded; charset = UTF-8",
    "Referer": "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND"
}

# result = requests.post(url, headers=headers, json={'key': 'value'}).text
result = requests.post(url, params=params, headers=headers).text
# print(result)

data = json.loads(result, encoding='utf-8')
# print(data)
print(json.dumps(data, ensure_ascii=False, indent=2))

print(len(data['jsonList']))
for j in data['jsonList']:
    print(j["ROAD_NAME"], j["APT_NAME"], j["JIBUN_NAME"])

# with open("./data/rtm1.json", mode="w") as file:
#     file.write(html)
    
