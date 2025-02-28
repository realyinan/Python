import copy

a = [1, 2, 3]
b = [11, 22, 33]
c = [6, 7, a, b]
x = c

# 测试id(c)和id(e)
d = copy.deepcopy(c)
print(id(x))
print(id(c))
print(id(d))
print('**********')  

# 测试id(c[2])和id(a)
print(id(a))
print(id(c[2]))
print(id(d[2]))  

a[2] = 22
print(c)
print(d)

# 深拷贝：拷贝一个对象时，只要发现对象有可变类型就会对该对象到最后一个可变类型的每一层对象就行拷贝，对每一层拷贝的对象都会开辟新的内存空间进行存储。
