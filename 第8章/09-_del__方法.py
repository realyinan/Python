class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("创建对象时会被自动调用")

    def __del__(self):
        print("对象被销毁时会被自动调用")


p1 = Person("Tom", 20)
