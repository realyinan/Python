# 1. 生成如下列表 [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8],[0,3,6,9,12]]

# 方法一
list1 = []
for i in range(4):
    list2 = []
    for j in range(5):
        list2.append(i * j)
    list1.append(list2)
print(list1)

# 方法二
list1 = [[i*j for j in range(5)] for i in range(4)]
print(list1)