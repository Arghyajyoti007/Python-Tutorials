# Magic/Dunder Methods in Python
class Employee:
    name = "Harry"
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

e = Employee()
print(e.name)
print(len(e))
