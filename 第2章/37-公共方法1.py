# 运算符	描述	支持的容器类型
# +	合并	字符串、列表、元组
# *	复制	字符串、列表、元组
# in	元素是否存在	字符串、列表、元组、字典、集合
# not in	元素是否不存在	字符串、列表、元组、字典、集合

# 1.合并
# 字符串
str1 = 'hello'
str2 = 'world'
print(str1 + str2)  # helloworld

# 列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # [1, 2, 3, 4, 5, 6]

# 元组
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)

# 2.复制
# 字符串
str1 = 'hello'
print(str1 * 3)  # hellohellohello

# 列表
list1 = [1, 2, 3]
print(list1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 元组
tuple1 = (1, 2, 3)
print(tuple1 * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 3.元素是否存在
# 字符串
str1 = 'hello'
print('h' in str1)  # True
print('h' not in str1)  # False

# 列表
list1 = [1, 2, 3]
print(1 in list1)  # True
print(1 not in list1)  # False

# 元组
tuple1 = (1, 2, 3)
print(1 in tuple1)  # True
print(1 not in tuple1)  # False

# 字典
dict1 = {'name': 'Tom', 'age': 20}
print('name' in dict1)  # True
print('name' not in dict1)  # False

# 集合
set1 = {1, 2, 3}
print(1 in set1)  # True
print(1 not in set1)  # False