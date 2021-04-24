data = 1000

with open("t.txt", "w", encoding="euc-kr") as f:
    f.write(str(data))

with open("t.bin", "wb") as f:
    f.write(bytearray(   [int(data / 5), int(data / 5)]    ))

soup.select('data[seq=0]')