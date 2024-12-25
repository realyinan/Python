def func(num):
    num += 1
    print(num)
    
# 定义一个全局变量
a = 10
# 调用函数
func(a)
# 在全局作用域中打印a
print(a)

# 不可变类型在函数中，局部或全局的改变对外部和内部都没有任何影响。