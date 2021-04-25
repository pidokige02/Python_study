import os
# OS utility 성 함수를 모아놓은 부분임
#  
def clear():
    # os.system('cls' if os.name == 'nt' else 'clear')  # 아래 함수와  같은 기능임

    if os.name == 'nt':
        os.system('CLS')
    else:  # posix
        os.system('clear')
