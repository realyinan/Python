list1 = ['a', 'b', 'c', 'd']
list2 = ['x', 'y', 'z']


# append() 增加指定数据到列表中
list1.append('e')
print(list1)

# extend() 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
list1.extend(list2)
print(list1)
list3 = ["Hello"]
list3.extend('Python')
print(list3)

# insert() 指定位置新增数据
list1.insert(2, '3')
print(list1)