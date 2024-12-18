set1 = {10, 20, 30, 40, 50}

# add()方法：向集合中增加一个元素（单一）
set1.add(60)
print(set1)

# update()方法：向集合中增加序列类型的数据（字符串、列表、元组、字典）
set1.update([1, 2, 3])
print(set1)
set1.update('abc')
print(set1)