# Assignment 40: Fibonacci Sequence
# Create a Python program that generates and prints the first n terms of the Fibonacci sequence using a for loop.
# The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two previous terms.

first_num = 0
second_num = 1
sum = 0

# 0 1 1 2 3 5 8 13
n = int(input("Enter the range of numbers: "))
print(first_num)
print(second_num)
for i in range(n):
    sum = first_num + second_num
    first_num = second_num
    second_num = sum
    print(sum)



