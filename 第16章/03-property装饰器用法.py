# property用来修饰函数的, 目的是简化代码开发
# 装饰器方式:
# @property 修饰获取值的方法
# @方法名.setter 修饰设置值的方法


class Student(object):
    def __init__(self):
        self.__name = ''

    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self, name):
        self.__name = name

    


if __name__ == "__main__":
    s = Student()
    s.set_name = "小明"
    print(s.get_name)
    