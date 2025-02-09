def outer():
    num = 20
    def inner():
        nonlocal num
        num = 10
    print(f"修改前: {num}")
    inner()
    print(f"修改后: {num}")


outer()

# nonlocal 用于在嵌套函数中声明一个变量，使其绑定到外部但非全局作用域的变量。它常用于闭包，允许修改外部（但不是全局）作用域的变量。