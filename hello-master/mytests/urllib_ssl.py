import myurls
import sys
import urllib.request as ur
import os.path as path
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sys.path.insert(0, '../ttt')


# url = "http://www.weather.go.kr/repositary/image/rdr/img/RDR_CMP_WRC_201901081255.png"
#url = "https://image-comic.pstatic.net/webtoon/721457/9/20190107143230_15d34308650589a5dbb7a30910dab27d_IMAG01_1.jpg"
url = "https://postfiles.pstatic.net/MjAxOTAxMDdfNDEg/MDAxNTQ2ODU4ODU3ODYw.l4ImUZRkFLZcZe8qSKlVSXTLm3exI1HO3EPLhrhJrWQg.TgaaqwebK1tPtLGFApi8IUhxptRe5YtFEdu-AA43bVUg.JPEG.play_joo1021/KakaoTalk_20190107_195407491.jpg?type=w773"


saveFile = "./ttt/test.png"
# mem = ur.urlopen(url, context=ctx).read()
mem = ur.urlopen(url, context=myurls.sslContext()).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")
