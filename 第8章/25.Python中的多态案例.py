class Dog():
    def work(self):
        print("I can work")

class ArmyDog(Dog):
    def work(self):
        print("Chasing the enemy")

class DrugDog(Dog):
    def work(self):
        print("Drug search")


class Person():
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DrugDog()

me = Person()
me.work_with_dog(ad)
me.work_with_dog(dd)



# + 多态体现

# +加号只有一个，但是不同的对象调用+方法，其返回结果不同。

# 如果加号的两边都是数值类型的数据，则加号代表运算符

# 如果加号的两边传入的是字符串类型的数据，则加号代表合并操作，返回合并后的字符串

# 'a' + 'b' = 'ab'

# 如果加号的两边出入序列类型的数据，则加号代表合并操作，返回合并后的序列

# [1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]