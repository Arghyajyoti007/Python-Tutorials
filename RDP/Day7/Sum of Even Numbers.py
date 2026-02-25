# Assignment 32: Sum of Even Numbers
# Write a Python program that calculates and prints the sum of all even numbers from 1 to 50 using a while loop.

i = 1
sum_num = 0
while True:
    if i%2 == 0:
        sum_num += i

    if i == 51:
        break
    i += 1

print(sum_num)
