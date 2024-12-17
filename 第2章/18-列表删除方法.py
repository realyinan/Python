list1 = ['1', '2', '3', '4', '5', '6']

# del 列表[索引]	删除列表中的某个元素
del list1[1]
print(list1)

# pop()	删除指定下标的数据(默认为最后一个)，并返回该数据
print(list1.pop())
print(list1)
print(list1.pop(1))
print(list1)

# remove() 移除列表中某个数据的第一个匹配项
list1.remove('4')
print(list1)

# clear() 清空列表，删除列表中的所有元素，返回空列表。
list1.clear()
print(list1)