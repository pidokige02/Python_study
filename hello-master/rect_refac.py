class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s)
        else:
            return s


class 사각형:
    x, y = 0, 0

    name = "사각형"

    def __init__(self):
        print("사각형 created")

    def input_data(self, msg):
        datum = input(msg)
        data = datum.split(',')  # 2,3
        self.x = Casting.to_int(data[0])
        self.y = Casting.to_int(data[1])
        # return self.넓이()

    def 새넓이(self):
        return self.x * self.y


class 직사각형(사각형):
    name = "직사각형"

    def __init__(self):
        # super(직사각형, self).__init__()
        print("직사각형 created")

    def 넓이(self, x, y):
        return Casting.to_int(x) * Casting.to_int(y)


class 평행사변형(사각형):
    name = "평행사변형"

    def 넓이(self, x, y):
        return Casting.to_int(x) * Casting.to_int(y)


while True:
    print("--------------------------------------------------------------")
    # all_rects = ['직사각형', '평행사변형']
    all_rects = [직사각형(), 평행사변형()]
    rect_type = input("\n사각형의 종류는?\n 1) 직사각형\n 2) 평행사변형\n (quit: q) >> ")
    if (rect_type == 'q'):
        break

    rect = all_rects[Casting.to_int(rect_type) - 1]
    rect.input_data("가로와 세로는?? (usage: 가로,세로)")
    result = rect.새넓이()
    print("result=", result)

    # if rect_type == '1':
    #     # rect1 = 직사각형()
    #     가로_세로 = rect.set_msg("가로와 세로는?? (usage: 가로,세로)")
    #     print("1111>>", 가로_세로, 가로_세로.split(','))
    #     가로, 세로 = 가로_세로.split(',')
    #     print("2222>>", 가로, 세로)
    #     결과 = rect1.넓이(가로, 세로)
    #     print("직사각형의 넓이는 {}입니다".format(결과))

    # else:
    #     # rect2 = 평행사변형()
    #     밑변_높이 = input("밑변와 높이는?? (usage: 밑변,높이)")
    #     밑변, 높이 = 밑변_높이.split(',')
    #     결과 = rect2.넓이(밑변, 높이)
    #     print("평행사변형의 넓이는 {}입니다".format(결과))
