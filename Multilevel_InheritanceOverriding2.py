# Base class
class Vehicle:
    def start(self):
        return "Vehicle starts"

# Derived class
class Car(Vehicle):
    def start(self):
        return "Car starts"

# Sub-derived class
class SportsCar(Car):
    def start(self):
        return "Sports Car starts"

# Creating an instance of SportsCar
sports_car = SportsCar()
print(sports_car.start()) # Calls the start method of SportsCar class