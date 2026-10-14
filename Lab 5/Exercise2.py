# Class to demonstrate Operator Overloading
class ComplexNumber:
    
    # Constructor
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overloading + operator
    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    # Overloading - operator
    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    # Overloading string representation
    def __str__(self):
        # Handle negative imaginary properly
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

# Creating objects
c1 = ComplexNumber(3,2)
c2 = ComplexNumber(1,7)

# Addition
add_result = c1 + c2
print("After Add:", add_result)

# Subtraction
sub_result = c1 - c2
print("After Subtract:", sub_result)