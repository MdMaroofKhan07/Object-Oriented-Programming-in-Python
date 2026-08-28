class Dog:
    species = "Canine" # Class attribute
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute
dog1 = Dog("Buddy", 3) # Create an instance of Dog
dog2 = Dog("Charlie", 5) # Create another instance of Dog
# Access instance and class attributes
print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)
# Access class attribute directly
print(Dog.species)