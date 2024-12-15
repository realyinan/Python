import random

num = random.randint(1, 10)

while True:
    your_num = int(input("请输入数字: "))
    if your_num == num:
        print("猜对了")
        break
    elif your_num > num:
        print("猜大了")
    else:
        print("猜小了")