# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name # Attribute common to all animals
    def speak(self):
        return f"{self.name} makes a sound." # Method common to all animals

# Derived class (Child class) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks." # Overriding the speak method for Dog

# Another Derived class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows." # Overriding the speak method for Cat

# Creating instances of Dog and Cat
dog = Dog("Rocky")
cat = Cat("Tom")

# Calling the speak method on Dog and Cat instances
print(dog.speak()) # Output: Rocky barks.
print(cat.speak()) # Output: Tom meows