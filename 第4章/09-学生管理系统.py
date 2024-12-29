students = []

def menu():
    print('-'*40)
    print('1、添加学员信息')
    print('2、删除学员信息')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、遍历所有学员信息')
    print('6、保存数据到文件')
    print('7、退出系统')
    print('-' * 40)

def add_student():
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    mobile = input('请输入学生手机号：')

    student = {}
    student['name'] = name
    student['age'] = age
    student['mobile'] = mobile

    global students
    students.append(student)
    print(f"学生信息{student}添加成功！")

def get_all():
    global students
    for student in students:
        print(f"姓名: {student['name']}, 年龄: {student['age']}, 手机号: {student['mobile']}")

def del_student():
    name = input("请输入要删除的学生姓名: ")
    global students
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print(f"学生{student}删除成功！")
            break
    else:
        print(f"学生{name}不存在！")
    
def edit_student():
    name = input("请输入要修改的学生姓名: ")
    global students
    for student in students:
        if student['name'] == name:
            student['name'] = input("请输入新的姓名: ")
            student['age'] = int(input("请输入新的年龄: "))
            student['mobile'] = input("请输入新的手机号: ")
            print(f"学生{student}修改成功！")
            break
    else:
        print(f"学生{name}不存在！")

def search_student():
    name = input("请输入要查询的学生姓名: ")
    global students
    for student in students:
        if student['name'] == name:
            print(f"姓名: {student['name']}, 年龄: {student['age']}, 手机号: {student['mobile']}")
            break
    else:
        print(f"学生{name}不存在！")

def save_data_to_file():
    global students
    f = open('./第4章/data.txt', 'w', encoding='utf-8')
    f.write(str(students))
    f.close()
    print("信息已保存成功")

def load_data():
    f = open('./第4章/data.txt', 'r', encoding='utf-8')
    global students
    students = eval(f.read())
    f.close()

load_data()
while True:
    menu()
    user_choice = input('请输入您的选择：')

    if user_choice == '1':
        add_student()
    elif user_choice == '2':
        del_student()
    elif user_choice == '3':
        edit_student()
    elif user_choice == '4':
        search_student()
    elif user_choice == '5':
        get_all()
    elif user_choice == '6':
        save_data_to_file()
    elif user_choice == '7':
        break

# 在循环内加载数据可能覆盖用户在本次运行中对数据的修改。比如，用户添加了新学生，但下一次循环又重新加载了原始数据，导致添加操作被“撤销”。