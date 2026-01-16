# Single Inheritance
class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species

    def makeSound(self):
        print("Sound made by the animal")

class Cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,"Cat")
        self.breed = breed
    def makeSound(self):
        print("Maow!!")

c = Cat("Pussy","PussyCat")
c.makeSound()