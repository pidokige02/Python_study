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
        <tbody>
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
        <tbody>
    </table>
'''

soup = BeautifulSoup(html, 'html.parser')
tds = [tr.select('td:nth-of-type(2)') for tr in soup.select('tbody tr')]
pprint(tds)
