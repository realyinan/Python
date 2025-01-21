# 某班级有5名学生，他们的学号、姓名和英语成绩如下表所示，此数据存储在student_scores.txt文件中，请编写一个程序，完成如下功能：

# 1，计算每个学生的平均成绩。

# 2，输出平均成绩最高的学生信息。

# 3，要求使用面向对象完成此需求，即，创建学生对象用于存储学号、姓名、得分，提供计算平均分方法等。

# +------+--------+------+------+------+
# | 学号 |  姓名   | 语文  | 数学  | 英语 |
# +------+--------+------+------+------+
# | 001  | 张三   |  85  |  90  |  78  |
# | 002  | 李四   |  92  |  88  |  95  |
# | 003  | 王五   |  88  |  92  |  85  |
# | 004  | 赵六   |  78  |  85  |  90  |
# | 005  | 小明   |  95  |  92  |  88  |
# +------+--------+------+------+------+
# student_scores.txt文本内容如下

# 学号,姓名,语文,数学,英语
# 001,张三,85,90,78
# 002,李四,92,88,95
# 003,王五,88,92,85
# 004,赵六,78,85,90
# 005,小明,95,92,88


class Student():
    def __init__(self, student_id, name, chinese, math, english):
        self.student_id = student_id
        self.name = name
        self.scores = {
            "chinese": chinese,
            "math": math,
            "english": english
        }

    def calculate_average(self):
        return sum(self.scores.values()) / len(self.scores)
    
    def __str__(self):
         return f"学号: {self.student_id}, 姓名: {self.name}, 平均成绩: {self.calculate_average():.2f}"


def read_students_from_file(file_path):
    students = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]
        for line in lines:
            data = line.strip().split(',')
            student = Student(
                student_id=data[0],
                name=data[1],
                chinese=int(data[2]),
                math=int(data[3]),
                english=int(data[4])
            )
            students.append(student)

    return students


def find_top_student(students):
    return max(students, key=lambda student: student.calculate_average())
    # 这里 key=lambda student: student.calculate_average() 表示对每个学生对象，调用其 calculate_average() 方法（计算平均成绩），并使用该方法的返回值作为比较依据。
    # max() 函数的 key 参数允许我们指定一个函数，该函数会作用于列表中的每个元素，用于比较大小


if __name__ == "__main__":
    file_path = "./第8章/student_scores.txt"
    students = read_students_from_file(file_path)
    print("每个同学的成绩")
    for student in students:
        print(student)
    print("----------------------------")
    print("最好的同学")
    top_student = find_top_student(students)
    print(top_student)