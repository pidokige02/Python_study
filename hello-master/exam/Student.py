g_grades = ['A', 'B', 'C', 'D', 'F']
g_grades.reverse()

class Student:
    grade = ''

    def __init__(self, line):
        name, gender, age, score, addr = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
        self.addr = addr

    def __str__(self):
        return "{}**\t{}\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade, self.addr)

    def make_params(self):
        return (self.name[0] + '**', self.make_gender(), self.make_age(), self.make_grade(), self.make_addr())
        
    def make_gender(self):
        return 'F' if self.gender == '여' else 'M'

    def make_age(self):
        try:
            iage = int(self.age) // 10
            return "{:d}0대".format(iage)
        except:
            return "알수없음"

    def make_addr(self):
        addrs = self.addr.split(' ')
        gu = ''
        dong = ''
        for i in addrs:
            if i.find('구') == (len(i) - 1):
                gu = i
            elif i.find('동', 1) == (len(i) - 1):
                # print(i, i.find('동', 1), len(i))
                dong = i

        return "{} {}".format(gu, dong)

    def make_grade(self):
        if self.score == 100:
            return 'A+'
        elif self.score < 50:
            return 'F'
        else:
            return g_grades[self.score // 10 - 5]
