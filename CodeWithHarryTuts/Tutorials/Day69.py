# Class Methods
class Employee:
    company = "Apple"
    def show(self):
        print(f"The Name is {self.name} and company is {self.company}")

    @classmethod # to change the class variable
    def changeCompany(cls,newCompany):
        cls.company = newCompany





e1 = Employee()
e1.name="Arghya"
e1.changeCompany("Tesla")
e1.show()

