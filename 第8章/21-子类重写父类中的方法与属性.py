class Animal(object):
    def eat(self):
        print("I can eat")

    def call(self):
        print("I can call")



class Dog(Animal):
    def call(self):
        print("汪汪")

class Cat(Animal):
    def call(self):
        print("喵喵")


cat = Cat()
cat.eat()
cat.call()
print("---------------------")

dog = Dog()
dog.eat()
dog.call()