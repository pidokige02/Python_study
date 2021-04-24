import urllib.request as ur

url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm={}&endTm={}"

rng = input("Input the start and end date>> ")
rngs = rng.split(" ")
if len(rngs) < 2:
    print("Input Data Error!!")
    exit()

startdt = rngs[0]
enddt = rngs[1]
print(startdt, enddt)
url = url.format(startdt, enddt)
print(url)

saveFile = "./images/weather22.html"
ur.urlretrieve(url, saveFile)
print("OK!")
