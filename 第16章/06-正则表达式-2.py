import re

# \d 代表一个数字, [0-9]
# \d 代表除数字以外的任意字符, [^0-9]
# ? 数量词: 前面的内容出现0次 或者 1次
# * 数量词: 前面的内容出现0 ~ n次
# + 数量词: 前面的内容出现1 ~ n次


result = re.match(pattern="[0-9].*", string="1hmit")
print(result.group())
result = re.search(pattern="[0-9].*", string="a1hmit")
print(result.group())
result = re.search(pattern="\d.*", string="a1hmit")
print(result.group())