int_numbers = range(-5, 6)
# f = filter(lambda x: x[0] == '김', int_numbers)
f = filter(lambda x: x * 2, int_numbers)
m = map(lambda x: x * 2, int_numbers)

print("f=", list(f) )   # list 화 시켜서 출력을 한다.
# true 인 것만 출련하므로 0만 빠진다.
print("m=", list(m))

