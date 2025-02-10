def logging(flag):
    def decorator(fn):
        def inner(*args, **kwargs):
            if flag == '+':
                print('正在进行加法运算')
            elif flag == '-':
                print('正在进行减法运算')
            result = fn(*args, **kwargs)
            return result
        return inner
    return decorator


@logging('+')
def sum_num(num1, num2):
    return num1 + num2

@logging('-')
def sub_num(num1, num2):
    return num1 - num2

# decorator = logging("+")  # 先调用 logging("+")，返回 decorator
# sum_num = decorator(sum_num)  # 再用返回的 decorator 处理 sum_num

print(sum_num(4, 3))
print(sub_num(4, 3))
