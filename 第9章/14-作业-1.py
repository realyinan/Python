# 假设你是一名网站开发者，你需要设计一个函数 login_counter()，用于统计用户登录的次数和最近一次登录的时间。

# 要求：

# login_counter() 返回一个闭包 login()。
# 每次调用 login()，它将累加用户登录的次数，并记录最近一次登录的时间。
# 需要返回一个字典，包含累计的登录次数（total_count）和最近一次登录的时间（last_login_time）。
# 设计思路：

# 在 login_counter() 函数外部定义一个变量 count，用于记录累计的登录次数。
# 在 login_counter() 函数内部定义一个变量 last_login，用于记录最近一次登录的时间戳。
# 在 login() 函数内部更新 count 和 last_login 的值，并返回字典形式的结果。
import time

def login_counter():
    count = 0
    last_login = None
    def login():
        nonlocal count, last_login
        count += 1
        last_login = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return {'count': count, 'last_login': last_login}
    return login

func = login_counter()
print(func())
time.sleep(0.5)
print(func())
time.sleep(0.5)
print(func())
time.sleep(0.5)
print(func())
time.sleep(0.5)


    