# 1 1 2 3 5 8 13 21 .

# 程序调用自身的编程技巧称为递归（ recursion）。递归做为一种算法在程序设计语言中广泛应用，它通常==把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解==，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。

# =① 明确你这个函数想要干什么==

# 如：求斐波那契数列

# ==② 寻找递归结束条件==

# 如：就是在什么情况下，递归会停止循环，返回结果

# ==③ 找出函数的等价关系式==

# 如：斐波那契数列，第n位 f(n) = f(n-1) + f(n-2)

def Fibonacci(n):
    if n <= 1:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)

print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))
print(Fibonacci(8))
print('-------------------------')


def fn(n):
    if n <= 0:
        return 1
    else:
        return fn(n-1)*n
    
print(fn(5))
print(fn(6))
print(fn(10))
