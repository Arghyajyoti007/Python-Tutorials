# Class and Objects

class Human:

    # property
    # name = 0
    # age = 0
    # x = 5**10

    # init() executed when an class is initialized
    def __init__(self, name, age):
        # self is reference to current instances of the class
        self.name = name
        self.age = age

    def method(self):
        print("Hi, my name is: " + self.name)
        print("My age is: " + str(self.age))


h1 = Human("Ajay", 52)
h2 = Human("Anil", 50)

# print(h1.name)
# print(h1.age)
h1.method()
h2.method()


# to change values
h1.name= "Rahul"
h1.method()

# to delete an object
del h2
# h2.method()



# to create an empty class
class Animals:
    pass
