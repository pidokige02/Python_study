import urllib.request as ur
import timeit
start = timeit.default_timer()

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

saveFile = "./data/weather.xml"

data = ur.urlopen(url).read()
# text = data.decode('utf-8')
with open(saveFile, mode="wb") as file:
    file.write(data)

print("OK!", (timeit.default_timer() - start) * 1000)
