# dir, __dict__ and help method in Python
x = [1,2,3]
print(dir(x))
print(x.__add__)
y=(1,2,3)
print(dir(y))

# __dict__
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e = Employee("Arghya",122222)
print(e.__dict__)

# help()
print(help(Employee))