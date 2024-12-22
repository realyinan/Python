# 函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。

def user_info(name, age, address):
    print(f'您的姓名是{name}，年龄是{age}，地址是{address}')

user_info(address='上海市', age=20, name='张三')