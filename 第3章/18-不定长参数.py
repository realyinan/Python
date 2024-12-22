def fun(*args, **kwargs):
    result = 0
    for i in args:
        result += i

    for i in kwargs.values():
        result += i

    return result

print(fun(10, 20, 30, num3=100, num4=500))