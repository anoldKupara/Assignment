class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def displayInfo(self):
        print(f"Vehicle Brand: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, number_of_doors):
        super().__init__(brand, speed)
        self.number_of_doors = number_of_doors

    def displayInfo(self):
        print(f"Car Brand: {self.brand}, Speed: {self.speed} km/h, Doors: {self.number_of_doors}")

class Bike(Vehicle):
    def __init__(self, brand, speed, has_gear):
        super().__init__(brand, speed)
        self.has_gear = has_gear

    def display_info(self):
        print(f"Bike Brand: {self.brand}, Speed: {self.speed} km/h, Has Gear: {self.has_gear}")

# Creating objects
my_car = Car("Toyota", 180, 4)
my_bike = Bike("Yamaha", 120, True)

my_car.displayInfo()
my_bike.displayInfo()
