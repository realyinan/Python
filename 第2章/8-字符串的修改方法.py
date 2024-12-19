# replace()	返回替换后的字符串  字符串.replace(要替换的内容, 替换后的内容, 替换的次数-可以省略)

str1 = 'Hello Linux'
print(str1.replace('Linux', 'Python'))
str2 = 'Hello Linux and Hello Linux'
print(str2.replace('Linux', 'Python', 2))  