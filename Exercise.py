from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):
    def __init__(self, c):
        self.color = c

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self):
        pass


# Derived Class
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side

    def get_area(self):
        return self.side * self.side
    
class Rectangle(Shape):
    def __init__(self,c,l,b):
        super().__init__(c)
        self.l = l
        self.b = b
    def get_area(self):
        return self.l * self.b
    
class Triangle(Shape):
    def __init__(self,c,base,height):
        super().__init__(c)
        self.base = base
        self.height = height
    def get_area(self):
        return (1/2) * self.base * self.height
    
class Circle(Shape):
    def __init__(self,c,radius):
        super().__init__(c)
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius * self.radius
    
square = Square("red", 5.0)
rectangle = Rectangle("golden",2,3)
triangle = Triangle("green",5,4)
circle = Circle("blue",9)

shapes = [square,rectangle,triangle,circle]

for shape in shapes:
    print(shape.get_color(),shape.get_area())