code = input("请输入交易密码: ")
print(code)
print(type(code))
print(isinstance(code, str))

# 当程序执行到`input`，等待用户输入，输入完成之后才能继续向下执行。
# 在Python中，`input`接收用户输入后，一般存储到变量，方便使用。
# 在Python中，`input`会把接收到的任意用户输入的数据都当做字符串处理。
