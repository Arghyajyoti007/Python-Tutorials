# Assignment 37: Sum of Even Numbers
# Write a Python program that calculates and prints the sum of all even numbers from 1 to 50 using a for loop.

total_even = 0
for i in range(1,51):
    if i % 2 == 0:
        total_even += i
print(total_even)
