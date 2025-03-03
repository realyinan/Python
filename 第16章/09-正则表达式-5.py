import re

# ^ 代表正则的开头
# $ 代表正则的结尾


res = re.search(pattern="^\dit", string="1it")
print(res)
res = re.search(pattern="^\dit", string="a1it")
print(res)
res = re.search(pattern="[xyz]$", string="itx")
print(res)
res = re.search(pattern="[xyz]$", string="itxd")
print(res)

# 校验手机号. 规则: 1. 长度必须是11位, 2. 第二位数字必须是3, 4, 5, 6, 7, 8, 9, 2. 第一位数字必须是1
res = re.match(pattern="^1[3-9]\d{9}$", string="15838745437")
print(res)