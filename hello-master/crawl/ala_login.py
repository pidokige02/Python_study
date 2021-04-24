import requests
from bs4 import BeautifulSoup

session = requests.session()

loginUrl = "https://www.aladin.co.kr/login/wlogin_popup.aspx?SecureOpener=1"

headers = {
    "Referer": loginUrl,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

params = {
    'Email': 'shjeon77',
    'Password': 'x8whq7Kjq5wPNpD',
    'Action': '1',
    'ReturnUrl': '',
    'ReturnUrl_pop': '',
    'SecureLogin': 'false',
    'snsUserId': '0',
    'snsType': '0',
    'snsAppId': '1'
}

res = session.post(loginUrl, data=params, headers=headers)
res.raise_for_status()
res2 = session.get('https://www.aladin.co.kr/account/wmaininfo.aspx?pType=MyAccount&start=we')
res.raise_for_status()
soup = BeautifulSoup(res2.text, "html.parser")
helloBox = soup.select_one('div.hellow_box_title')
print(helloBox)

