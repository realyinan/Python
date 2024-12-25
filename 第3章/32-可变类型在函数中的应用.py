def func(names):
    names.append('赵六')
    
# 定义一个全局变量
list1 = ['张三', '李四', '王五']
# 调用函数
func(list1)

print(list1)

# 可变类型在函数中，如果在全局或局部中对可变类型进行增删改操作，其外部和内部都会受到影响。