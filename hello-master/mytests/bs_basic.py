from bs4 import BeautifulSoup

html = '''
<html>
    <head>
        <title>테스트</title>
    </head>
    <body>
        <h1>테스트용 HTML</h1>
        <p>첫번째 p태그<b>STRONG</b>ㅎㅎㅎ</p>
        <p>두번째 p태그</p>
        <div class="container well">
            <p>ppp</p>
            <a href="#" id="aaa">AAA</a>
            <section><p>qqq</p></section>
        </div>
        <div>두번째 DIV</div>
        <ul>
            <li><a href="https://naver.com">naver</a></li>
            <li><a href="https://daum.net">daum</a></li>
        </ul>
    <body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
body = soup.html.body
h1 = body.h1
p1 = body.p
strong_text = p1.next.next.next
p2 = p1.next_sibling.next

# container = soup.select('div.container')
container = body.select_one('div.container')
# container = body.find('div')   # cf. body.find_all('div')
# container = body.find('div', class_="container")
classes = container.attrs['class']

# aaa = container.find('a', id="aaa")
aaa = container.a

ul = soup.select("ul li")
for li in ul:
    print(li.a.string)

print("h1>>", h1)
print("p1>>", p1, ", next=", p1.next)
print("strong>>", strong_text)
print("p2>>", p2)
print("container>>", container, ", classes=", classes)
print("aaa>>", aaa)

print("--------------------------------------------")
# print(soup.select('p + p'))
print(soup.select('div  p'))
# print(soup.select('div a'))
# print(soup.select('li:nth-of-type(2)'))
# print(soup.select('div[class~=container]'))
# print(soup.select('div[class*=con]'))