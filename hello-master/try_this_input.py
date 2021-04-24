cmd = input("Input(usage: 이름,나이,성별)>> ")
# print("aaaa=" + cmd + ".")

error_msg = "정확히 입력해 주세요!!!"

# 1.값이 존재여부 체크
if cmd == '':
    print(error_msg)
    exit()

# 2. , 가 있는지 체크
# if ',' not in cmd:
if cmd.find(',') == -1:
    print(error_msg)
    exit()

is_not_exists_comma = True
for i in cmd:   #abc
    if i == ',':
        is_not_exists_comma = False
        break

if is_not_exists_comma:
    print(error_msg)
    exit()

cmds = cmd.split(',')
# 3. 3개의 값이 있는지!
if len(cmds) != 3:
    print(error_msg)
    exit()

outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다"
print(outmsg.format(cmds[0], cmds[1], cmds[2]))
