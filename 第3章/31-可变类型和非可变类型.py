# 非可变类型

# 数值（int整型、float浮点类型）

# bool类型（True和False）

# 字符串类型（str）

# 元组（tuple 1,2,3）

# 非可变类型就是在内存中，内存地址一旦固定，其变量的值就没办法发生任何改变了



# 可变类型

# 列表（list [1, 2, 3]）

# 字典（dict {key:value})

# 集合（set {1, 2})

# 可变类型就是在内存中，其内存地址一旦固定，其变量的值是可以发生改变的

a = 10
print(id(a))
a = 20
print(id(a))
print('-----------------')

b = [1, 2, 3]
print(id(b))
b.append(4)
print(id(b))