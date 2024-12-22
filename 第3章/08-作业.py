# 定义函数findall，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)

def findall(s, sub):
    n = len(sub)
    res = []
    for i in range(len(s) - n + 1):
        if s[i:i+n] == sub:
            res.append(i)
    return tuple(res)

print(findall("helloworldhellopythonhelloc++hellojava", "hello"))