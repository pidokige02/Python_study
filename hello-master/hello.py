print("Hello World!")

fruits = ['오렌지', '사과', '바나나']
fruits.extend(['aa'])

i, sum = 0, 0
while (i >= 0):
    i += 1
    if (i > 10 and i < 20):
      continue

    sum += i;
    if (i == 100):
        print("End!!", sum)
        break
