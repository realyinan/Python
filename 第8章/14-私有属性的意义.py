class Person(object):
    def __init__(self, name):
        self.name = name
        self.__salary = 18000

    def set_salary(self, salary):
        if 0 < salary <= 50000:
            self.__salary = salary
        else:
            print("设置有误")

    def get_salary(self):
        print(self.__salary)

