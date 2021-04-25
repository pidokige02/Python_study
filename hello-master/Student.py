# class refactoring 기법으로 화일 이름을 대문자로 하여 만든다.

g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()  # list 순서를 뒤집는다.

class Student:
    grade = ''

    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')  # 
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)
        # 이**  gender  age 

    def make_grade(self):
        if self.score == 100:
            self.grade = 'A+'
        elif self.score < 50:
            self.grade = 'F'
        else:
            self.grade = g_grades[self.score // 10 - 5] # // 은 몫을 구하는 연산자
