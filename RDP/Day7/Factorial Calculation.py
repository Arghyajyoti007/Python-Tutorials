# Assignment 34: Factorial Calculation
# Write a Python program that calculates and prints the factorial of a given number using a while loop.
# Ensure the program handles non-negative integer input.

user_input = int(input("Enter a Number: "))
multiple_ans = 1

while user_input != 0:
    multiple_ans = multiple_ans * user_input
    user_input -= 1

print(f"Factorial : {multiple_ans}")
