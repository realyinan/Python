# Python拆包：就是把元组或字典中的数据单独的拆分出来，然后赋予给其他的变量。

def return_num():
    return 1, 2

a, b = return_num()
print(a, b)

dict1 = {'name':'小明', 'age':18}

a, b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])