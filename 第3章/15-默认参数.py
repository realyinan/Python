# 缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）。

def user_info(name, age, address='深圳市'):
    print(f'您的姓名是{name}，年龄是{age}，地址是{address}')

user_info('张三', 20)
user_info('李四', 30, '北京市')