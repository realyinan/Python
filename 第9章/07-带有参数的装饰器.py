def logging(fn):
    def inner(n1, n2):
        print("输出日志")
        fn(n1, n2)
    return inner


@logging
def sum_num(num1, num2):
    print(num1 + num2)


sum_num(10, 20)