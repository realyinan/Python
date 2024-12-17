str1 = 'i am tom, nice to meet you'
print(str1.title())

username = input("请输入用户名: ")
password = input("请输入密码: ")

if username.lower() == 'admin' and password.lower() == 'admin88':
    print('登录成功')
else:
    print('登录失败')