class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("这是一个初始化方法")

p1 = Person("Tom", 20)
print(p1.name)
print(p1.age)

p2 = Person("Jerry", 30)
print(p2.name)
print(p2.age)

# 创建对象时, 会自动调用__init__方法