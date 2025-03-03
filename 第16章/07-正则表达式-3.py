import re

s1 = "习近平新时代中国特色社会主义思想哈哈哈哈嘿嘿嘿"
res = re.sub(pattern=r"嘿|哈", repl="1", string=s1)
print(res)

res = s1.replace("哈哈哈哈嘿嘿嘿", "111111")
print(res)
