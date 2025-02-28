# 在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。

def outer():
    b = 20
    def inner():
        print(b)
    return inner

f = outer()
f()

# 闭包的作用：正常情况下，当执行outer()的时候，函数内部的变量b = 20，会随着函数的outer函数的结束而被垃圾回收机制所回收。所以闭包的真正作用：就是可以在全局作用域中，实现间接对局部变量进行访问。

# 由于闭包引用了外部函数的变量，则外部函数的变量没有及时释放，消耗内存。


# 函数名存放的是函数所在内存空间的地址 （大白话：函数名代表函数入口地址）
# 函数名()执行函数名所存放空间地址中的代码 （大白话：函数名()代表函数调用: 直接调用）
# 函数名可像普通变量一样赋值, 赋值后的结果与原函数名作用是一样的 
