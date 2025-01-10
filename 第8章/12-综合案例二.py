# 案例2：小明体重75.0公斤，小明每次跑步会减掉0.50公斤，小明每次吃东西体重增加1公斤。
# 分析：① 对象：小明② 属性：姓名、体重③ 方法：跑步、吃东西

class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f"{self.name}跑步后的体重是{self.weight}")

    def eat(self):
        self.weight += 1
        print(f"{self.name}吃东西后的体重是{self.weight}")


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()