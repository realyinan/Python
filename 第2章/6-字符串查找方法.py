# find(要搜索的内容) 检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则返回-1。
# index(要搜索的内容) 检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则则报异常。

str1 = 'Hello World'
print(str1.find('World'))
print(str1.find('Linux'))
print('='*8)
print(str1.index('World'))
print(str1.index('Linux'))


