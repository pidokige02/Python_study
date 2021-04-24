def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return a

    return a / b


def input_calc():
    cmd = input("수식을 입력하세요(usage: 2 + 3)> ")
    if (cmd == 'q'): exit()

    cmds = cmd.split(' ')

    # a = cmds[0]
    # op = cmds[1]
    # b = cmds[2]

    a, op, b = cmds
    # print("a=",a, ", op=", op, ", b=", b)

    a, b = int(a), int(b)

    # outType = "{:d}"
    if op == '+':
        r = plus(a, b)

    elif op == '-':
        r = minus(a, b)

    elif op == '*':
        r = mul(a, b)

    else:
        r = div(a, b)


    if op == '/':
        print("Answer is {:.2f}".format(r))

    else: 
        print("Answer is {:d}".format(r)) 


while True:
    input_calc()