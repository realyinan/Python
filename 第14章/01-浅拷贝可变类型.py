import copy

a = [1, 2, 3]
b = [11, 22, 33]
c = [6, 7, a, b]
x = c

# 测试id(c)和id(e)
d = copy.copy(c)
print(id(x))
print(id(c))
print(id(d))
print('**********')  # id(c)和id(d)值不一样, 说明拷贝了第1层

# 测试id(c[2])和id(a)
print(id(a))
print(id(c[2]))
print(id(d[2]))  # id(c[2])和id(a)值一样, 说明没有拷贝第二层数据

a[2] = 22
print(c)
print(d)

# 浅拷贝只对可变类型的第一层对象进行拷贝，对拷贝的对象开辟新的内存空间进行存储，且不会拷贝对象内部的子对象。