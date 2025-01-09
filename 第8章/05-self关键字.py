class Person(object):
    def eat(self):
        print(self)
        print("吃炸鸡")

    def drink(self):
        print("喝可乐")


p1 = Person()
print(p1)
p1.eat()

# 在类中，有一个特殊关键字self，其指向类实例化对象本身。