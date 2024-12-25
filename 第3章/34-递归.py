# 1 1 2 3 5 8 13 21 .

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
    if n == 0:
        return 1
    else:
        return fn(n-1)*n
    
print(fn(5))
print(fn(6))
