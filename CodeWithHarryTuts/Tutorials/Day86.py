# Walrus Operator
# Allows to assign value within expression
a = True
print(a:=False)

foods = list()
while(food := input("What do you like?") != "quit"):
    foods.append(food)