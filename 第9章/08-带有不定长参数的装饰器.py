def logging(fn):
    def inner(*args, **kwargs):
        print('输出日志')
        fn(*args, **kwargs)
    return inner

@logging
def  sum_num(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for i in kwargs.values():
        result += i
    print(result)


sum_num(1, 2, 3, a=1, b=2, c=3)
