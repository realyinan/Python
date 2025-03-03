import re

# {n} 恰好n次
# {n,} 
# {n,m}
# ? 数量词: 前面的内容出现0次 或者 1次
# * 数量词: 前面的内容出现0 ~ n次
# + 数量词: 前面的内容出现1 ~ n次
res = re.match(pattern="\d*it", string="123321it")  # Y
res = re.match(pattern="\d*it", string="it")  # Y
res = re.match(pattern="\d+it", string="it")  # N


res = re.match(pattern="\d{3}it", string="234it")  # Y
res = re.match(pattern="\d{3}it", string="2345it")  # N
res = re.match(pattern="\d{3,}it", string="2345it")  # Y
res = re.match(pattern="\d{3,6}it", string="234it")  # Y
res = re.match(pattern="\d{3,6}it", string="2345it")  # Y
res = re.match(pattern="\d{3,6}it", string="23456it")  # Y




