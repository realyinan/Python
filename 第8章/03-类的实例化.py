# 创建一个类
class Person(object):
    def eat(self):
        print("吃炸鸡")

    def drink(self):
        print("喝可乐")


# 类的实例化
xiaoming = Person()
print(xiaoming)
xiaoming.drink()
xiaoming.eat()


