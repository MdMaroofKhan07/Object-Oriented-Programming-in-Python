class Employee:
    def __init__(self,id,salary):
        self.id = id
        self.salary = salary

    def getInfo(self):
        return f"EmployeeID:{self.id} Salary:{self.salary}"
    
class SalesEmployee(Employee):
    def __init__(self,id,salary,sales=0):
        super().__init__(id,salary)
        self.sales = sales

    def getInfo(self):
        return f"EmployeeID:{self.id} Salary:{self.salary} Sales:{self.sales}"
    
obj1 = Employee(103,70000)
obj2 = SalesEmployee(103,70000,300)
print(obj1.getInfo())
print(obj2.getInfo())