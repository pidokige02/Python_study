from bs4 import BeautifulSoup
import requests
import urls

# bbsUrl = "https://blog.naver.com/korea_diary/221433346994"
bbsUrl = "https://blog.naver.com/d_ahae/221436343740"
bbsUrl = "https://blog.naver.com/kkomataku/221437665643"
bbsUrl = "https://blog.naver.com/baekmg1988/221405485574"
html = requests.get(bbsUrl).text
soup = BeautifulSoup(html, 'html.parser')

ifrSel = "iframe#mainFrame"
ifr = soup.select_one(ifrSel)
src = ifr.get('src')
orgUrl = urls.urljoin( urls.getHostname(bbsUrl, True), src )

orgHtml = requests.get(orgUrl).text
orgSoup = BeautifulSoup(orgHtml, 'html.parser')

titleSel = "div.se-title-text span"
titleEle = orgSoup.select_one(titleSel)
if not titleEle:
    titleEle = orgSoup.select_one('div.se_title')

if titleEle:
    title = titleEle.text.strip()
else:
    title = 'Title 못찾음!! ' + bbsUrl

# print("-->", title)
# exit()

sel = "img.se-image-resource"
imgs = orgSoup.select(sel)
# print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

print("--------------------------------------", title)
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open("./images/" + urls.getFilename(src), "wb") as file:
        file.write(requests.get(src).content)
