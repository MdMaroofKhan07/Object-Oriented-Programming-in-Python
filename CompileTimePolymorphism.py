class Calculator:
    def add(self,*args):
        return sum(args)
    
calc = Calculator()
print(calc.add(5,10))
print(calc.add(5,10,15))
print(calc.add(1,2,3,4))
