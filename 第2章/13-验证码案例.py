# 练习题3：给定一个字符串，如：
# mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# 使用所学的知识，从字符串中随机取出4个字符，生成验证码。

import random

mystr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

code = ''

for i in range(4):
    code += mystr[random.randint(0, len(mystr)-1)]

print(code)