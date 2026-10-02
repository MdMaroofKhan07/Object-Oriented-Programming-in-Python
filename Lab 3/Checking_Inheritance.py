# Base class
class Animal:
    pass

# Derived classes
class Dog(Animal):
    pass
class Cat(Animal):
    pass

# Checking if an object is an instance of a class
dog = Dog()
cat = Cat()

print(isinstance(dog, Dog)) # Output: True
print(isinstance(dog, Animal)) # Output: True
print(isinstance(cat, Cat)) # Output: True
print(isinstance(cat, Dog)) # Output: False

# Checking if a class is a subclass of another
print(issubclass(Dog, Animal)) # Output: True
print(issubclass(Cat, Animal)) # Output: True
print(issubclass(Dog, Cat)) # Output: False
