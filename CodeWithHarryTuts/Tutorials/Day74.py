# method overriding

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self,x,y):
        return self.x * self.y

class Circle:
    def __init__(self, red):
        self.red = red

    def area(self):
        return 3.14* self.red * self.red

c = Circle(5)
print(c.area())