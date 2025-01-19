class Tool():
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1

    @classmethod
    def show_count(cls):
        print(cls.count)


t1 = Tool("锤子")
t1.show_count()
Tool.show_count()


# 类方法就是针对类对象定义的方法，在类方法中可以直接访问类属性或者调用其他类方法。
