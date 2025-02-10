def logging(fn):
    def inner(*args, **kwargs):
        print("输出log")
        result = fn(*args, **kwargs)
        return result
    return inner


@logging
def sum_num(num1, num2):
    return num1 + num2

@logging
def sub_num(num1, num2):
    return num1 - num2


print(sum_num(4, 3))
print(sub_num(4, 3))
