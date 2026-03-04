# Assignment 38: Multiplication Table
# Create a Python program that generates and prints the multiplication table for a given number.
# Use a for loop to iterate from 1 to 10 to generate the table for that number.

user_input = int(input("Enter the Number: "))

for i in range(1,10):
    print(f"{i}*{user_input} = {user_input*i}")



