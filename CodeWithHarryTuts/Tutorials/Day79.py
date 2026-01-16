# Multiple Inheritance
class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class Dancer:
    def __init__(self,danceType):
        self.danceType = danceType
    def show(self):
        print(self.danceType)

class EmployeeDancer(Employee,Dancer):
    def __init__(self,name,dance):
        self.name = name
        self.danceType=dance

o = EmployeeDancer("Ajay","Break Dance")
print(o.name)
print(o.danceType)
o.show() # Whichever class is being passed first in class EmployeeDance, the show method from that class will be executed.

