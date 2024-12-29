def fn1():
    return 100

print(fn1())
print(fn1)
print('-----------------')

res = lambda a, b: a + b
print(res(1, 2))
print('-----------------')

# 带默认参数
res = lambda a, b = 2: a + b
print(res(1))
print(res(1, 3))
print('-----------------')

# 不定长参数
res = lambda *args: args
print(res(1, 2, 3))
print('-----------------')

res = lambda **kwargs: kwargs
print(res(a=1, b=2, c=3))
print('-----------------')

# 带三目运算符
res = lambda a, b: a if a > b else b
print(res(1, 2))
print('-----------------')

students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

students.sort(key=lambda x: x['name'])
print(students)

students.sort(key=lambda x: x['age'], reverse=True)
print(students)