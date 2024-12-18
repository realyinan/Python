students = []
while True:
    print('-' * 40)
    print('[1] 增加学员信息')
    print('[2] 查询学员信息')
    print('[3] 删除学员信息')
    print('[4] 退出系统')
    print('-' * 40)

    choice = input('请输入你的选项: ')

    if choice == '1':
        name = input('请输入学生的姓名: ')
        age = input('请输入学生的年龄: ')
        tel = input('请输入学生的电话: ')
        student = {}
        student['name'] = name
        student['age'] = age
        student['tel'] = tel
        students.append(student)
        print(f"学生{student['name']}添加成功")

    elif choice =='2':
        for i in students:
            print(i)

    elif choice == '3':
        name = input('请输入要删除的学生姓名: ')
        for i in students:
            if i['name'] == name:
                students.remove(i)
                print(f'已删除{name}')
                break
        else:
            print('查无此人')

    elif choice == '4':
        break
    else:
        print('输入错误请重新输入')