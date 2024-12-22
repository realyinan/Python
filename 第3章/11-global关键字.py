num = 10

def fun():
    # 声明变量num为全局变量
    global num
    num = 20

fun()
print(num)