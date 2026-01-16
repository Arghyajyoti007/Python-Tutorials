x=y=z="Orange"
print(x)
print(y)
print(z)

multiLineString = """These 
is
a 
multiline
String"""

print(multiLineString)

multiLineString = '''These 
is
a 
multiline
String'''
print(multiLineString)

#String is python is an Array
x = "Hello, World!"
print(x)
print(x[0])
print(x[10])

for a in x:
    print(a)

print(len(x))

#to check if substring present in string
print("World" in x)
print("Like" in x)

#Slice the String
print(x[2:5])
print(x[:5])
print(x[:])
print(x[-5:-2])


#To modify the String
print(x.upper())

d="  blank   "
print(d.strip())

#replace a string
print(x.replace("H","Y"))

#Split
print(x.split(","))

#Concatination
a="Hi"
b="you"
print(a+" "+b)


