import random

computer = random.randint(0, 2)

player = int(input("请输入你的出拳信息(石头 - 0, 剪刀 - 1, 布 - 2): "))

if (player == 0 and computer == 1) or (player == 1 and computer == 2) or(player == 2 and computer == 0):
    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")

a = 2
b = 3
temp = a
a = b
b = temp
