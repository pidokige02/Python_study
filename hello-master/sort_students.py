class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):  # default 로 된것을 override 한 것임 
        # explicitly 하게 호출되지는 않아도 string 출력시 자동으로 호출이됨
        return "{}:{}".format(self.name, self.score)



students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]

fss = filter(lambda stu: stu.score >= 20, students)
for fs in fss:
    print(fs)

print("=========================")

def print_students():
    print("--------------------")
    for s in students:
        print(s)


students = sorted(students, key=lambda stu: stu.score)
# sorted는 내장함수
# key=lambda stu: stu.score key 값으로 stu 를 받아서 score 를 return 함
# 즉 score 로 sorting 한 것임.
print_students()

students.sort(key=lambda stu: stu.score)
# sort는 list 의 member 함수임.
print_students()
