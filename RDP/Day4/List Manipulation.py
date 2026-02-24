# Assignment 19: List Manipulation: Write a Python program that does the following:
# Initializes an empty list.
# Asks the user to enter a series of numbers (use a loop for this).
# Appends each entered number to the list.
# After the user is done entering numbers, display the list.

lists = []

while True:
    number = int(input("Enter a Number : "))
    lists.append(number)

    quit = input("Enter 'q' to quit : ")
    if quit == "q":
        break

print(lists)
