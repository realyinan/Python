list1 = [i for i in range(6)]
print(list1)
set1 = {i for i in range(6)}
print(set1)
print('-------------')



my_generator = (i for i in range(6))  # 这个不是元组推导式, 而是生成器(对象)
print(my_generator)
print(type(my_generator))  # <class 'generator'>

# 从生成器中获取数据
print(next(my_generator))
print(next(my_generator))
print("-------------")

for i in my_generator:
    print(i)


# 根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。数据不是一次性全部生成出来，而是使用一个，再生成一个，可以节约大量的内存。
