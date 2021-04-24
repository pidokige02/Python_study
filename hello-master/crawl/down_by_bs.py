from bs4 import BeautifulSoup
import requests

# url = "https://search1.kakaocdn.net/thumb/C232x336.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fcontentshub%2Fsdb%2Fe04c93361ba66f52150d4a0665a9309f53c221a91f2c572b323fb09927a723da"

url = "https://postfiles.pstatic.net/MjAxOTAxMDNfMjYw/MDAxNTQ2NTA4NzYwNjQ3.fVyIE3nPM6zmvVZuaJG9tSAqzopYNzUGUpPHR9v86hMg.Hyq_lVTVWz-pnaSC3TZ8ue4iJOfJMgkOFVSQozQdYqUg.PNG.korea_diary/천안_호두과자.png?type=w966"

img = requests.get(url).content

saveFile = "./images/aaa.png"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")



