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
        super().__init__(brand, model, color)  # 这样可以复用父类的属性初始化代码，避免重复写逻辑。
        self.battery = battery
        

    def run(self):
        print("I can run with electricity")



telsa = ElectricCar("telsa", "粉色", "Model S", 70)
print(telsa.battery)
print(telsa.brand)
print(telsa.color)
print(telsa.model)
telsa.run()
