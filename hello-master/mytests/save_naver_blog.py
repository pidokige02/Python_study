import requests, json
from bs4 import BeautifulSoup
import pymysql, re

'''
drop table if exists BlogPost;
drop table if exists Blogger;

create table Blogger(
    blogid varchar(64) not null primary key,
    name varchar(128),
    bloglink varchar(255)
);

create table BlogPost(
    id int not null auto_increment primary key,
    title varchar(255) not null,
    blogid varchar(64) not null,
    postdate varchar(8),
    posturl varchar(255)
);

alter table BlogPost add constraint foreign key(blogid) references Blogger(blogid);
'''

def get_conn():
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db='dadb',
        # cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

headers = {
    "X-Naver-Client-Id": "dRgjJjP4QdJyV3qR8oqS",
    "X-Naver-Client-Secret": "uB4v_zPuG0"
}

params = {
    "display": 100,
    "start": 1,
    "sort": "date",
    "query": "파이썬"
}

url = "https://openapi.naver.com/v1/search/blog"
html = requests.get(url, params=params, headers=headers).text
jsonData = json.loads(html)
# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

SqlBlogger = "insert into Blogger(blogid, name, bloglink) values(%s, %s, %s)"
SqlBlogPost = "insert into BlogPost(title, blogid, postdate, posturl) values(%s, %s, %s, %s)"
Domain = 'blog.naver.com'
LenDomain = len(Domain)

def getBlogid(str):
    print(str)
    if Domain in str:
        return str[str.index(Domain) + LenDomain + 1:]
    else:
        return re.sub("(http(s)*|:|/)", '', str)

bloggers = []
posts = []
for i in jsonData['items']:
    blogid = getBlogid(i['bloggerlink'])
    # print(i['title'], i['bloggername'], i['postdate'], i['link'])
    print(getBlogid(i['bloggerlink']))

# with conn:
#     cur = conn.cursor()
