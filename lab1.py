class Car:
    def __init__(self, make, model):
        self._make = make  
        self.__model = model  

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make)  
my_car.drive()


class ElectronicCar(Car):
    
    def __init__(self, make, model, battery_capacity):
    
        super().__init__(make, model) 
        self.battery_capacity = battery_capacity  
    
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electronic_car = ElectronicCar("Tesla", "Model Y", 75)
my_electronic_car.drive()
my_electronic_car.charge()