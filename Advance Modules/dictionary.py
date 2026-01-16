#unordered, changeable, amd DO NOT ALLOW duplicate values
#store in the form of key and value
dictt = {
    "name" : "Raj",
    "age" : "22",
    "vehicle" : "Bike",
    "DOB" : "12-12-2001",
    #do not allow duplicate means that it update the key to it's new value
    "vehicle" : "Car",
    "books" : ["A","B","C"],
    "student" : True
}
print(dictt)
print(len(dictt))
print(type(dictt))

#access
x=dictt["vehicle"]
print(x)

x = dictt.get("vehicle")
print(x)

#to change
dictt["vehicle"] = "Lambo"
print(dictt)
dictt.update({"vehicle" : "BMW"})
print(dictt)

dictt["color"] = "gray"
print(dictt)

#to delete
dictt.pop("vehicle")
print(dictt)

