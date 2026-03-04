# Assignment 39: Prime Number Checker
# Write a Python program that checks if a given number is prime.
# Use a for loop to test if the number is divisible by any integer from 2 to the square root of the number.
# Print whether the number is prime or not.

def isPrime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 6
        return True

input_num = int(input("Enter the Number to check: "))
if isPrime(input_num):
    print(f"{input_num} is Prime Number")
else:
    print(f"{input_num} is Not Prime Number")
