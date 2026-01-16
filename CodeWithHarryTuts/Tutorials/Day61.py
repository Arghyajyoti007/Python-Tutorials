# Inheritance
class Employee:
    def __init__(self, name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The Name of Emp : {self.id} is {self.name}");

class Prgrammer(Employee):
    def showLanguage(self):
        print("The Language is Python")

e1 = Employee("Rohan Das",400)
e1.showDetails()
e2 = Prgrammer("Arghya",55)
e2.showDetails()
e2.showLanguage()