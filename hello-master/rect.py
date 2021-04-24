def to_int(s):
   if type(s) == str:
       return int(s)
   else:
       return s


class 사각형:
   x, y = 0, 0

   def __init__(self):
       print("사각형 created")


class 직사각형(사각형):
   def 넓이(self, x, y):
       return to_int(x) * to_int(y)


class 평행사변형(사각형):
   def 넓이(self, x, y):
       return to_int(x) * to_int(y)


while True:
   print()
   rect_type = input("사각형의 종류는?\n 1) 직사각형\n 2)평행사변형\n (quit:q) >> ")
   if (rect_type == 'q'):
       break

   if rect_type == '1':
       rect1 = 직사각형()
       가로_세로 = input("가로와 세로는?? (usage: 가로,세로)")
       print("1111>>", 가로_세로, 가로_세로.split(','))
       가로, 세로 = 가로_세로.split(',')
       print("2222>>", 가로, 세로)
       결과 = rect1.넓이(가로, 세로)
       print("직사각형의 넓이는 {}입니다".format(결과))

   else:
       rect2 = 평행사변형()
       밑변_높이 = input("밑변와 높이는?? (usage: 밑변,높이)")
       밑변, 높이 = 밑변_높이.split(',')
       결과 = rect2.넓이(밑변, 높이)
       print("평행사변형의 넓이는 {}입니다".format(결과))
