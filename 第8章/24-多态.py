# 多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果。

class Fruit(object):
    def makejuice(self):
        print('i can make juice')

class Apple(Fruit):
    # 重写父类方法
    def makejuice(self):
        print('i can make apple juice')

class Banana(Fruit):
    # 重写父类方法
    def makejuice(self):
        print('i can make banana juice')

class Orange(Fruit):
    # 重写父类方法
    def makejuice(self):
        print('i can make orange juice')

# 定义一个公共接口（专门用于实现榨汁操作）
def service(obj):
    # obj要求是一个实例化对象，可以传入苹果对象/香蕉对象
    obj.makejuice()

# 调用公共方法
service(Orange())
service(Banana())
service(Apple())