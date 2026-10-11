class Flyable:
    def fly(self):
        return "This object can fly."
    
class Swimmable:
    def swim(self):
        return "This object can swim."
    
class Duck(Flyable,Swimmable):
    def quack(self):
        return "Duck quacks."
    
duck = Duck()

print(duck.fly())
print(duck.swim())
print(duck.quack())
