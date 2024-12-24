list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
list2 = ['X', 'Y', 'Z']

# 方法一
list3 = []
for i in list2:
    for j in list1:
        list3.append(i + j)

print(list3)

# 方法二
list3 = [i + j for i in list2 for j in list1]
print(list3)