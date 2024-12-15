# 编写一个程序，实现一个简单的登录系统。用户需要输入用户名和密码进行登录，最多允许输入错误的次数为3次。如果用户名和密码都正确，则输出 "登录成功！" 并结束程序；如果输入错误次数超过了3次，则输出 "登录失败，错误次数过多，账号已锁定"。

# 要求：

# 正确的用户名为 "admin"，正确的密码为 "password"。
# 编写程序实现以上需求，使用 while...else... 语句来判断用户登录是否成功，并限制最大错误次数为3次。

i = 0
while i < 3:
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if username == "admin":
        if password == "password":
            print("登录成功！")
            break
        else:
            print("密码错误！请重新输入。")
    else:
        print("用户名错误！请重新输入。")

    i += 1