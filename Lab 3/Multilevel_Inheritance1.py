# Multilevel Inheritance
class Dog:
    def __init__(self, name):
        self.name = name
    def displayName(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog): # Inheritance
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador): # Multilevel Inheritance
    def guide(self):
        print(f"{self.name} Guides the way!")

guideDog = GuideDog("Max")
guideDog.displayName()
# guideDog.sound()
guideDog.guide()