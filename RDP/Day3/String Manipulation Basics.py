# Assignment 11:
# String Manipulation Basics Create a Python program that takes a user's full name as input and prints it in reverse order
# (last name, first name).
# Then, count and display the total number of characters in the full name.
# Finally, extract and display the initials of the first and last names.

full_name = input("Enter Full Name: ").split()

first_name = full_name[0]
last_name = full_name[-1]

print(last_name)
print(last_name, first_name)

