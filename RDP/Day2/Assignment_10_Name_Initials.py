# Assignment 10:
# Name Initials Write a program that takes a full name
# as input and outputs the initials in uppercase.
# For example, if the input is "John Doe", the output
# should be "JD".

name = input("Enter full name: ")
# print(full_name)

space_ind = name.find(" ")
splitted_name = name.split(" ")

if len(splitted_name) == 1:
    print("Hello " + splitted_name[0].upper())
elif len(splitted_name) == 2:
    print("Hello " + name[0].upper() + name[space_ind+1].upper())
elif len(splitted_name) > 2:
    print("Hello " + splitted_name[0][0].upper() + splitted_name[-1][0].upper())