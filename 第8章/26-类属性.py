# Python中，属性可以分为==实例属性==和==类属性==。
# 类属性就是 类对象中定义的属性，它被该类的所有实例对象所共有。通常用来记录 与这类相关 的特征，类属性 不会用于记录 具体对象的特征。
class Person():

    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.count +=1

p1 = Person("lili", 23)
p2 = Person("nana", 24)
print(p1.count)
print(p2.count)

print(Person.count)