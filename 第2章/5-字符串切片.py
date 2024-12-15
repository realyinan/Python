# 切片其实很简单，只顾头来尾不管，步长为正正向移，步长为负则逆向移
num1 = '0123456789'
print(num1[2:5:1])  # 234
print(num1[2:5])  # 234
print(num1[:5]) # 01234
print(num1[0:])  # 0123456789
print(num1[:])  # 0123456789
print(num1[::2])  # 024680
print(num1[:-1])
print(num1[-4:-1])
print(num1[-1:-4:-1])
print(num1[::-1])