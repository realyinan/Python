# 循环可以和else配合使用，else下方缩进的代码指的是==当循环正常结束之后要执行的代码。==
# 一旦break语句执行了，则else语句则不会输出。
i = 0
while i < 5:
    if i == 2:
        # break
        i += 1
        continue

    print('你好')
    i += 1
else:
    print('再见')