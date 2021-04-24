import urllib.request as ur
import timeit
start = timeit.default_timer()

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# url = "http://berryservice.net:8080/Berry/g/tests/12"

res = ur.urlopen(url)
data = res.read()

print("---->", timeit.default_timer() - start)

data = data.decode("utf-8")
print(data)

end = timeit.default_timer()
print("Elapsed time is", (end - start), "ms.")
