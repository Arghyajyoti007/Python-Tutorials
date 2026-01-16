# list can store strings numbers like integer, float etc and Boolean values

# list are ordered, changeable, and allow dupliactes

list = ["car", "bike", 90, 25.6, True, "bike", 'bike']
print(list)

print(len(list))
print(type(list))

# accessing
print(list[0])
print(list[5])

print(list[2:6]) #range


#changing element
print(list)
list[2] = "Bus"
print(list)

list[2:5] = ["ship", 10000, "changed"]
print(list)

#insert items : to add elements to a certain position
list.insert(3, "Jeep")
print(list)

#add items : to add at the end
list.append("Oranges")
print(list)

#delete items
list.remove("car")
print(list)



