# 1	len()	计算容器中元素个数
# 2	del或del()	根据索引下标删除指定元素
# 3	max()	返回容器中元素最大值
# 4	min()	返回容器中元素最小值
# 5	range(start, end, step)	生成从start到end（不包含）的数字，步长为 step，供for循环使用
# 6	enumerate()	函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

# 1.计算容器中元素个数
# 字符串
str1 = 'hello'
print(len(str1))  # 5

# 列表
list1 = [1, 2, 3]
print(len(list1))  # 3

# 元组
tuple1 = (1, 2, 3)
print(len(tuple1))  # 3

# 字典
dict1 = {'name': 'Tom', 'age': 20}
print(len(dict1))  # 2

# 集合
set1 = {1, 2, 3}
print(len(set1))  # 3

# 2.根据索引下标删除指定元素
# 列表
list1 = [1, 2, 3]
del list1[1]
print(list1)  # [1, 3]

# 字典
dict1 = {'name': 'Tom', 'age': 20}
del dict1['name']
print(dict1)  # {'age': 20}

# 3.返回容器中元素最大值
# 字符串
str1 = 'hello'
print(max(str1))  # o

# 列表
list1 = [1, 2, 3]
print(max(list1))  # 3

# 元组
tuple1 = (1, 2, 3)
print(max(tuple1))  # 3

# 4.返回容器中元素最小值
# 字符串
str1 = 'hello'
print(min(str1))  # e

# 列表
list1 = [1, 2, 3]
print(min(list1))  # 1

# 元组
tuple1 = (1, 2, 3)
print(min(tuple1))  # 1

# 5.生成从start到end（不包含）的数字，步长为 step，供for循环使用
for i in range(1, 10, 2):
    print(i)

# 6 emumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# 字符串
str1 = 'hello'
for index, value in enumerate(str1):
    print(index, value)

# 列表
list1 = [1, 2, 3]
for index, value in enumerate(list1):
    print(index, value)

# 元组
tuple1 = (1, 2, 3)
for index, value in enumerate(tuple1):
    print(index, value)

# 字典
dict1 = {'name': 'Tom', 'age': 20}
for index, value in enumerate(dict1):
    print(index, value)

# 集合
set1 = {1, 2, 3}
for index, value in enumerate(set1):
    print(index, value)

