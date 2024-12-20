def return_num():
    return 1
    return 2

# 只执行了第一个return，原因是因为return可以退出当前函数，导致return下方的代码不执行。
print(return_num())

# 在Python中，理论上一个函数只能返回一个结果。但是如果我们向让一个函数可以同时返回多个结果，我们可以使用return 元组的形式。
def return_num2():
    return 1, 2

print(return_num2())
print(type(return_num2()))