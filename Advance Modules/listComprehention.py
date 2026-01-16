#smaller line of code to create a new list from an existing list
fruits = ["Apple", "Banana", "Pinaple","Mango"]
newFruits = []
#creating a list of newFruits from fruits which have the letter 'a' in it
for x in fruits:
    if "a" in x:
        newFruits.append(x)

print(newFruits)

#in case of listComprehention

newFruits = [x for x in fruits if "i" in x]
print(newFruits)

newFruits = [x for x in fruits if x!="Banana"]
print(newFruits)

h = [x for x in range(10)]
print(h)

h = [x for x in range(10) if x<6]
print(h)

newFruits = [x.upper() for x in fruits]
print(newFruits)

newFruits = [x if x!="Banana" else "Oranges" for x in fruits]
print(newFruits)