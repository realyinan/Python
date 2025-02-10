def logging(fn):
    def inner(*args, **kwargs):
        print("输出日志")
        result = fn(*args, **kwargs)
        return result
    return inner



@logging  
def get_sum(num1, num2):
    return num1 + num2


# get_sum = logging(get_sum)

print(get_sum(1, 2))