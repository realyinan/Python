list1 = ['1', '2', '3', '4', '5', '6']
list1[2] = '100'
print(list1)

# reverse() 将数据序列进行倒叙排列
print(list1[::-1])
list1.reverse()
print(list1)

# sort() 对列表序列进行排序
list1.sort()
print(list1)