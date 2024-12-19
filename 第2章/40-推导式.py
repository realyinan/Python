# 推导式comprehensions（又称解析式），是Python的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列（一个有规律的列表或控制一个有规律列表）的结构体。 共有三种推导：列表推导式、集合推导式、字典推导式。

# 变量名 = [表达式 for 变量 in 列表]
# 变量名 = [表达式 for 变量 in 列表 if 条件]
# 变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]

list1 = [i for i in range(10)]
print(list1)

list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

# 案例：创建列表 => [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list1 = []
for i in range(1, 3):
    for j in range(3):
        list1.append((i, j))
print(list1)

list1 = [(1, j) for i in range(1, 3) for j in range(3)]
print(list1)