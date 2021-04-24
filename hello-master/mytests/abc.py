from bs4 import BeautifulSoup

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
companies = {}
data = {}
for i, tr in enumerate(soup.select('tr')):
    if i == 0:
        for j, th in enumerate(tr.select('th')):
            if j == 0: continue
            companies[th.text] = j - 1
    
    else:
        th = tr.select_one('th').text
        l = []
        for td in tr.select('td'):
            l.append(td.text)
        
        data[th] = l

while True:
    comp_item = input("회사와 항목을 입력하시오(q: 종료)>> ")
    if comp_item == 'q':
        break

    ci = comp_item.split(' ')
    idx = companies[ ci[0] ]
    item = ci[1]
    print("Result is", data[item][idx])
