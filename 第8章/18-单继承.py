class Car():
    def run(self):
        print("I can run")

class Gascar(Car):
    pass

class Electriccar(Car):
    pass


telsa = Electriccar()
telsa.run()

toyata = Gascar()
toyata.run()

# 在Python继承中，如A类继承了B类，B类又继承了C类。则根据继承的传递性，则A类也会自动继承C类中所有属性和方法（公共）