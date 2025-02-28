import copy

a = (1, 2, 3)
b = (11, 22, 33)
c = (6, 7, a, b)

d = copy.deepcopy(c)
print(id(c))
print(id(d))

# 不可变类型进行深拷贝不会给拷贝的对象开辟新的内存空间，而只是拷贝了这个对象的引用。

