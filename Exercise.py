# Base Class
class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def display(self):
        print(self.id, self.salary)


# Subclass
class SalesEmployee(Employee):
    def __init__(self, id, salary, sales):
        super().__init__(id, salary)
        self.sales = sales

    def display(self):
        print(self.id, self.salary, self.sales)


# Driver Code (taking input)
id = 14
salary = 30000
sales = 20

emp = Employee(id, salary)
sales_emp = SalesEmployee(id, salary, sales)

emp.display()
sales_emp.display()