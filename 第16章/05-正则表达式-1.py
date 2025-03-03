import re

# . 任意字符
# \. 取消.的特殊用法, 就是一个普通的.
# a 代表一个字符a
# [abc] a, b, c中任意一个字符
# [0-9]
# [a-zA-Z]
# [^abc] 除了a, b, c以外的任意一个字符


print(re.match(pattern=".it", string="ait"))
print(re.match(pattern=".it", string="aait"))
print(re.match(pattern=".it", string="aitb"))
print("-"*20)

res = re.match(pattern=".it", string="ait")
print(res.group())

res = re.match(pattern="[abc]it", string="cit")
print(res.group())

res = re.match(pattern="[^abc]it", string="git")
print(res.group())

