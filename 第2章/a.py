# 使用列表嵌套，完成8名老师随机分配3个办公室。
# 提示：
# 定义一个列表存放8位老师
# names = ['A','B','C','D','E','F','G','H']，
# 定义一个列表用来保存3个办公室offices = [[],[],[]]
import random

names = ['A','B','C','D','E','F','G','H']

offices = [[],[],[]]

for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

print(offices)
