def func():
    result = 0
    def inner(num):
        nonlocal result
        result += num
        print(result)
    return inner

f = func()
f(1)  #1
f(2)  #3
f(3)  #6