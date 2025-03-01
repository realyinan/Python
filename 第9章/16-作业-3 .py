# 根据如下说明，编写代码完成相关需求
# 1、
# 不带装饰器的基础功能：entry_grade
# 可以完成『成绩录入功能』
# 1.1可以重复录入成绩，默认所有输入都是合法的(1~100之间的数)
# 1.2当录入成绩为0时，结束成绩的录入
# 1.3将录入的成绩保存在列表中并返回给外界，例如：[90, 80, 50, 70]

# 2、
# 选择课程装饰器：choose_course
# 为『成绩录入功能』新增选择课程的拓展功能，达到可以录入不同学科的成绩
# 2.1可以重复输入要录入的学科名，然后就可以进入该门学科的『成绩录入功能』，录入结束后，可以进入下一门学科成绩录入
# 2.2当输入学科名为q时，结束所有录入工作
# 2.3将学科成绩保存在字典中并返回给外界，例如：{'math': [90, 80, 50, 70], 'english': [70, 50, 55, 90]}

# 3、
# 处理成绩装饰器：deal_fail
# 可以将所有录入的成绩按60分为分水岭，转换为 "通过" | "不通过"进行存储
# 3.1，如果只对原功能装饰，结果还为list返回给外界，例如：["通过", "通过", "不通过", "通过"]
# 3.2，如果对已被选择课程装饰器装饰了的原功能再装饰，结果就为dict返回给外界，
# 例如：{'math': ["通过", "通过", "不通过", "通过"],'english': ["通过", "不通过", "不通过", "通过"]}


def chose_course(func):
    def inner():
        courses = {}
        while True:
            course = input("请输入科目: ")
            if course == 'q':
                break
            grades = func()
            courses[course] = grades
        return courses
    return inner

def deal_fail(func):
    def inner():
        result = func()
        if isinstance(result, dict):
            for course in result:
                result[course] = ["通过" if grade >= 60 else "不通过"  for grade in result[course]]
        else:
            result = ["通过" if grade >= 60 else "不通过"  for grade in result]
        return result
    return inner


@chose_course
@deal_fail
def entry_grade():
    grades = []
    while True:
        grade = int(input("请输入成绩: "))
        if grade == 0:
            break
        grades.append(grade)
    return grades


print(entry_grade())