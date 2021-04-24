import requests
from bs4 import BeautifulSoup

userid = "shjeon77"
passwd = "x8whq7Kjq5wPNpD"

prm = "Email=shjeon77&Password=x8whq7Kjq5wPNpD&Action=1&ReturnUrl=&ReturnUrl_pop=&SecureLogin=false&snsUserId=0&snsType=0&snsAppId=1"
params = {
    "Email": "shjeon77",
    "Password": "x8whq7Kjq5wPNpD",
    "Action": "1",
    "ReturnUrl": "",
    "ReturnUrl_pop": "",
    # "SecureLogin": "false",
    "snsUserId": "0",
    "snsType": "0",
    "snsAppId": "1"
}

# loginUrl = "https://www.aladin.co.kr/login/wlogin_popup.aspx?SecureOpener=1"
loginUrl = "https://www.aladin.co.kr/login/wlogin.aspx?returnurl=/"
headers = {
    "Referer": loginUrl,
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    # "Cache-Control": "max-age=0",
    # "Host": "www.aladin.co.kr",
    # "Origin": "https://www.aladin.co.kr",
    # "Content-Type": "application/x-www-form-urlencoded",
    # "Cookie": "AladdinUser=UID=215894014&SID=g%2fobtd8PgeVqxSWVNSZHjw%3d%3d; AladdinSession=UID=215894014&SID=g%2fobtd8PgeVqxSWVNSZHjw%3d%3d; AladdinUS=CNn%2fqTCDJZVJcFjdZTQVPQ%3d%3d&USA=0; _ga=GA1.3.2006865119.1541813781; _BS_GUUID=FsYHj21a3rCDeBF9jeJblUNyLnFMZbEEEClYFn8J; ala_qs_use=1; _gid=GA1.3.1662983699.1547067108; _TRK_AUIDA_13987=524a75d235faba1ab5481341958af149:15; _TRK_ASID_13987=9a54fea219c8433df570df202bba42f8; _fbp=fb.2.1547067108689.2139031708; AladdinLogin=CNn%2fqTCDJZVJcFjdZTQVPQ%3d%3d; Aladin.AuthAdult=; __utma=256011483.2006865119.1541813781.1547067493.1547067493.1; __utmc=256011483; __utmz=256011483.1547067493.1.1.utmcsr=aladin.co.kr|utmccn=(referral)|utmcmd=referral|utmcct=/home/welcome.aspx; __utmt=1; __utmb=256011483.4.10.1547067493; _gat=1"
}

session = requests.session()
res = session.post(loginUrl, data=params, headers=headers)
# res = session.post(loginUrl, data=params)
res.raise_for_status()

################################################################
savedListUrl = "https://www.aladin.co.kr/shop/wsafebasket.aspx"
savedListUrl = "https://www.aladin.co.kr/account/wmaininfo.aspx?pType=MyAccount&start=we"

res2 = session.get(savedListUrl)
res2.raise_for_status()

soup = BeautifulSoup(res2.text, "html.parser")
print(soup.prettify())
myform = soup.select('#Myform')
print(myform)
print(soup.select('div.hellow_box_title p'))
