# 打印5x5正方形
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print('*', end=' ')
        j += 1

    print(' ')
    i +=1
print('='*20)

# 打印直角三角形
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print(' ')
    i +=1
print('='*20)

# 打印倒三角形

i = 5
while i > 0:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print(' ')
    i -= 1
print('='*20)


# 打印九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} x {i} = {j*i}", end='\t')
        j += 1
    print(' ')
    i += 1