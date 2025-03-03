class Student(object):
    def __init__(self):
        self.__name = '小刚'

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name


    # property 修饰类变量
    name = property(get_name, set_name)


if __name__ == "__main__":
    s = Student()
    print(s.name)
    s.name = "小明"
    print(s.name)
