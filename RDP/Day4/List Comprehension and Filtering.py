# Assignment 20 : List Comprehension and Filtering: Create a Python program that performs the following tasks:
# Initialize a list of numbers.
# Use list comprehension to create a new list that contains only the even numbers from the original list.
# Use another list comprehension to create a new list that contains squares of the numbers from the original list.
# Ask the user to input a number and use list comprehension to create a new list that contains only the numbers from
# the original list that are greater than the user's input.
# Display all three lists.

lists = [8, 78, 55, 45, 11, 14]

even_nums = [list_element for list_element in lists if list_element % 2 == 0]
square_nums = [square**2 for square in lists]
number_input = int(input("Enter a number: "))
greater_nums = [element for element in lists if element>number_input]

print(greater_nums)
print(even_nums)
print(square_nums)



