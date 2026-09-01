class Emp:
    def work(self):
        print("Employee works.")

class Manager(Emp):
    def work(self):
        print("Manager manages.")

class ProjManager(Manager):
    def work(self):
        print("Project Manager plans.")

obj = ProjManager()
obj.work()