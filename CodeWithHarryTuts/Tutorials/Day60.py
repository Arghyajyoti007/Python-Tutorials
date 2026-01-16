# Getter and Setter
class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)

    @property
    def ten_value(self):
        return 10*self.value

    @ten_value.setter
    def ten_value(self, new_val):
        self.value=new_val/10

obj = MyClass(10)
obj.ten_value=77
print(obj.ten_value)
obj.show()