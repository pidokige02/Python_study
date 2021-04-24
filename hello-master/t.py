im = "a,b,c"
arr = [m for m in im.split(',')]
print("arr=", arr)

outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다"
for val in arr:
    outmsg = outmsg.format(val, "{}", "{}")

print(outmsg.format(arr[0], arr[1], arr[2]))
