
# rows = int(input("请输入三角形的行数："))

# for i in range(rows, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# i = rows
# while i > 0:
#     j = 1
#     while j <= i:
#         print('*', end=' ')
#         j += 1
#     print(" ")
#     i -= 1

# 假设你正在开发一个简单的计算器程序，用户可以重复输入两个数字和一个运算符来执行基本的算术运算（加法、减法、乘法、除法），直到用户选择退出。


# while True:
#     method = input("请输入你要的运算(+, - * /), exit退出: ")
#     if method == 'exit':
#         break
#     else:
#         num1 = int(input("请输入num1: "))
#         num2 = int(input("请输入num2: "))
#         if method == '+':
#             print(num1 + num2)
#             continue
#         elif method == '-':
#             print(num1 - num2)
#             continue
#         elif method == '*':
#             print(num1 * num2)
#             continue
#         elif method == '/':
#             print(num1 / num2)
#             continue
 
# 题目 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了，第一天共摘了多少。

# 10 1
# 9 4
# 8 10
# 7 22
# 6 46

peaches = 1
for i in range(9, 0, -1):
    peaches = peaches * 2 + 2
print(peaches)
