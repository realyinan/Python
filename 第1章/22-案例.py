# 案例1：使用for循环，求1 ~ 100的和

s = 0
for i in range(1, 101):
    s += i
print(s)

s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s += i
print(s)