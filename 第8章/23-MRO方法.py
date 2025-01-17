class Car(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run')


class GasolineCar(Car):
    pass

class ElectricCar(Car):
    def __init__(self, brand, model, color, battery):
        super().__init__(brand, model, color)
        self.battery = battery
        

    def run(self):
        print("I can run with electricity")


print(ElectricCar.__mro__)
print(ElectricCar.mro())