list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 方法一
list2 = []
for i in list1:
    list2.append(i + 100)

print(list2)

# 方法二
list2 = [i + 100 for i in list1]
print(list2)