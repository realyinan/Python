# else语句：表示的是如果没有异常要执行的代码。
try:
    # print(1)
    print(1/0)
except ZeroDivisionError:
    print(2)
else:
    print(3)
finally:
    print("执行完毕")