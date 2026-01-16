
# tuple are ordered, un-changeable, and allow dupliactes
tuple = ("car", "bike", 90, 25.6, True, "bike")
print(tuple)
print(type(tuple))

#single element in a tuple is not going to work, it behaves like a string
tuple1 = ("car")
print(tuple1)
print(type(tuple1))

#if we really need a tuple to have single element, then we just need to add a comma (,) after the element
tuple1 = ("car",)
print(tuple1)
print(type(tuple1))

#to access
print(tuple[0])
print(tuple[1:5])

#to add
#tuple.append("Orange")
#print(tuple) #give error
#because tuple is unchangable we can not add, change or move the item


#to add an element in tuple.
#z = ("car", "bike", 90, 25.6, True, "bike", 'bike')
#y = list(z)
#y[1] = "Orange"
#y.append(5000)
#y.insert(1, "Hello")
#x = tuple(y)
#print(x)


