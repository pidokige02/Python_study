from bs4 import BeautifulSoup
import requests

html = '''
<html>
    <head>
        <title>테스트</title>
    </head>
    <body>
        <h1>테스트용 HTML</h1>
        <p>첫번째 p <b>STRONG</b>ㅎㅎ</p>
        <p>두번째 p태그</p>
        <div class="container well">
            <a href="#" id="aaa">AAA</a>
        </div>
        <div>두번째 DIV</div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
body = soup.html.body
h1 = body.h1
p1 = body.p
# print("h1=", h1, ", p1=", p1)
strong_text = p1.next.next.next
p2 = p1.next_sibling.next
# print(p1.next_sibling.next)

container = soup.select('div.container')
container = body.select_one('div.container')
container = body.find('div')   # cf. body.find_all('div')
# print("-->", container, type(container))
container = body.find('div', class_="container")
container = soup.select('div[class=container]')
container = soup.select('div[class~=container]')
print("-->", container, type(container))
# container_classes = container.attrs['class']

# aaa = container.find('a', id="aaa")
# aaa = container.a
