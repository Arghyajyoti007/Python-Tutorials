# super keyword in Python
class Parent:
    def parentClass(self):
        print("Parent")
class Child(Parent):
    # def parentClass(self):
    #     print("ParentChild")
    def childClass(self):
        print("Child")
        super().parentClass()
c = Child()
c.parentClass()
c.childClass()
