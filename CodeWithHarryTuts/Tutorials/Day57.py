class Person:
    name = "Arghya"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
# self means the object for which method is called

a = Person()
b = Person()
a.info()
a.name = "Toton"
a.occupation = "S/W AI"
b.name="Sonali"
b.occupation="HR"

a.info()
b.info()
