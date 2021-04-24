from functools import reduce
from Student import Student
# import Student

g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

students = []
with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append( Student(line) )    #Student 객체를 만들어 students list 에 append 함 

students.sort(key = lambda stu: stu.score, reverse = True)
m = map(lambda stu: stu.make_grade(), students) 
# 실제 map function 실행은 아래 list 호출시 실행이된다.
# 여기서는 구조만 잡아두는 것임
list(m)

def sumfn(x, y):
    if type(x) == int:
        return x + y.score
    else:
        return x.score + y.score


# total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)
total = reduce(sumfn, students)
avg = total / len(students)
print("총계, 평균>>>", total, avg)

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)

print("-----------------------------")
for s in students:
    if s.score >= avg:
        print(s.name, s.score)
