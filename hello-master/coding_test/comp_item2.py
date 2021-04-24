from bs4 import BeautifulSoup
from pprint import pprint

html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''

soup = BeautifulSoup(html, 'html.parser')

data = {}
indexes = {}
for i, tr in enumerate(soup.select('tr')):
    if i == 0:
        for j, th in enumerate(tr.select('th')):
            if j == 0: continue
            # data[th.text] = {'idx': j - 1}
            data[j - 1] = {'회사명': th.text}
            indexes[th.text] = j -1
    
    else:
        item_name = tr.select_one('th').text
        for k, td in enumerate(tr.select('td')):
            print(k, td)
            data[k][item_name] = td.text
        print("-------------")

# pprint(data)

# comp = "B사"
# item = "직원수"


while True:
    ival = input("회사와 아이템(종료:q)>> ")
    if ival == 'q':
        exit()

    ivals = ival.split(' ')

    comp = ivals[0]
    item = ivals[1]
    for k, v in data.items():
        print(k,v)
        if v['회사명'] == comp:
            print("result is", v[item])
            break
