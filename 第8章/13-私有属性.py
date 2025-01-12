class Girl(object):
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age


xiaomei = Girl("小美")
print(xiaomei.name)
print(xiaomei.get_age())
xiaomei.set_age(19)
print(xiaomei.get_age())

# 类中的私有属性和私有方法，不能被其子类继承。