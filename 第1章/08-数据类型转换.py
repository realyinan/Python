# ==int(x)==	将x转换为一个整数
# ==float(x)==	将x转换为一个浮点数
# complex(real [,imag ])	创建一个复数，real为实部，imag为虚部
# ==str(x)==	将对象 x 转换为字符串
# repr(x)	将对象 x 转换为表达式字符串
# ==eval(str)==	用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)	将序列 s 转换为一个元组
# list(s)	将序列 s 转换为一个列表
# chr(x)	用于将ASCII码（或Unicode码点）转为对应的字符。
# ord(x)	用于将字符转换为其对应的Unicode码点（整数）。对于ASCII字符，它会返回相应的ASCII码。
# hex(x)	将一个整数转换为一个十六进制字符串
# oct(x)	将一个整数转换为一个八进制字符串
# bin(x)	将一个整数转换为一个二进制字符串
print(chr(65))
print(chr(128512))
print(chr(19990))
print(ord('楠'))
print(ord('🤓'))
print(chr(129299))

print('*'*8)

print(hex(15))
print(oct(12))
print(bin(8))
print('*'*8)

print(eval('1+2'))
s = 'hello'
print(repr(int))
print(s)
print(complex(2, 3))