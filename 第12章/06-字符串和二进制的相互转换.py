# 数字, 英文字母, 特殊符号, 无论在什么码表中, 都只占1个字节
# 中文再GBK中占2个字节, 再utf-8中占3个字节
# b"内容" 这种写法只针对于字母, 数字, 特殊符号
# 码和表一定要对应

s1 = "凯特王妃"
print(s1.encode())
print(s1.encode("gbk"))
print(s1.encode("utf-8"))
print(type(s1.encode()))
print("---------------------------------")

s2 = "123@#$%"
print(s2.encode())
print(s2.encode("gbk"))
print(s2.encode("utf-8"))
print(type(s2.encode()))
print(type(s2))
print("---------------------------------")

b1 = b'\xe5\x87\xaf\xe7\x89\xb9\xe7\x8e\x8b\xe5\xa6\x83'
print(b1.decode())
print(b1.decode("utf-8"))