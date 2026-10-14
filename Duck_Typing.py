class Animal:
    def speak(self):
        return "I am an animal."
    
class Dog(Animal):
    def speak(self):
        return "Woofs!"
    
print(Dog().speak())

# Duck Typing

class Cat:
    def speak(self):
        return "Meow!"

# Function using Duck Typing 
# This function:
#   Accepts any object (animal)
#   Calls .speak() on it
#   Does NOT check class type  
def make_animal_speak(animal):
    return animal.speak()

print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))