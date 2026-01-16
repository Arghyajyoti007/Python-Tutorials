# Multilevel Inheritance
class Human:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name)
class Employee(Human):
    def __init__(self,name,id):
        Human.__init__(name)
        self.id=id

class Programmer(Employee):
    pass
