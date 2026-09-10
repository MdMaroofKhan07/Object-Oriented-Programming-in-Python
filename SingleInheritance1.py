# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name
    
    def displayName(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog): # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Example Usage
lab = Labrador("Buddy")
lab.displayName()
lab.sound()