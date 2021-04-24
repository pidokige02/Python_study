import urllib.request as ur


url = "http://www.weather.go.kr/repositary/image/sat/coms/coms_mi_le1b_ir1_k_201901080330.thn.png"

saveFile = "./images/weather1.png"
ur.urlretrieve(url, saveFile)
print("OK!")
