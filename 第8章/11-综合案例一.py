class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        if self.score >= 90:
            print(f"学生姓名: {self.name}, 成绩: {self.score}, 等级: A")
        elif self.score >= 80:
            print(f"学生姓名: {self.name}, 成绩: {self.score}, 等级: B")
        elif self.score >= 70:
            print(f"学生姓名: {self.name}, 成绩: {self.score}, 等级: C")
        elif self.score >= 60:
            print(f"学生姓名: {self.name}, 成绩: {self.score}, 等级: D")


s1 = Student("Tom", 90)
s1.print_score()

s2 = Student("Jerry", 80)
s2.print_score()