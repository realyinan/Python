class Gascar():
    def run_with_gas(self):
        print("Run with Gas")

class Electriccar():
    def run_with_electirc(self):
        print("Run with Electric")

class Mixedcar(Gascar, Electriccar):
    pass



car1 = Mixedcar()
car1.run_with_electirc()
car1.run_with_gas()