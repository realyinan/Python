def avg_num(a, b, c):
    """Return the average of three numbers."""
    return (a + b + c) / 3

help(avg_num)

print(avg_num(1, 2, 3))

# 案例2：编写一个函数，有一个参数str1，输入信息如'1.2.3.4.5'，使用函数对齐进行处理，要求最终的返回结果为'5-4-3-2-1'

def fun(str1):
    """Return the reversed string."""
    return '-'.join(str1.split('.')[::-1])

print(fun('1.2.3.4.5'))