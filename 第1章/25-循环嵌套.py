# 九九乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} x {i} = {i*j}", end='\t')
    print(' ')
print('='*20)

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} x {i} = {i*j}", end='\t')
        j += 1
    print(" ")
    i += 1