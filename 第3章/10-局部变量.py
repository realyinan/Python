def fun():
    num = 10
    print(num)

# 局部变量：在函数的调用过程中，开始定义，函数运行过程中生效，函数执行完毕后，销毁
fun()
print(num)