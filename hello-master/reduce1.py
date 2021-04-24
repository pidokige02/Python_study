from functools import reduce

lst = [1, 2, 3, 4]
product = lst[0]

for i, num in enumerate(lst):
    if i == 0: continue
    product = product + num

print("product1>>", product)

# 위의 여러 줄의 code가 한줄로 변경이 가능하다.
product2 = reduce(lambda x, y: x + y, lst)
# x는 이전 계산 결과값이고, y는 lst 의 새로계산할 next element임.
print("product2>>", product2)
