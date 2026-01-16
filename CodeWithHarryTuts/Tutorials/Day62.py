# Access Modifiers
# public, private, protected
class Employee:
    def __init__(self, private):
        self.name = "Arghya"
        self.__private = private # __private is

a = Employee()
print(a.name)