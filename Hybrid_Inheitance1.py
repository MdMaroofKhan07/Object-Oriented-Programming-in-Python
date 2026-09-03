class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def give_birth(self):
        print("Mammal gives birth")

class Bird(Animal):
    def lay_eggs(self):
        print("Bird lays eggs")

class Platypus(Mammal,Bird):
    pass

platypus = Platypus()
platypus.speak()
platypus.give_birth()
platypus.lay_eggs()
