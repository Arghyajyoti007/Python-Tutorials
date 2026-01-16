class Person:
    def __init__(self,name,occ):
        print("Hey I'm a person")
        self.name=name
        self.occ=occ
    # name = "Arghya"
    # occupation = "Software Developer"
    # networth = 10
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Name","Occ")
a.info()
