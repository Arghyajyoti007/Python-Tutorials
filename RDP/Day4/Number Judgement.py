# Assignment 17:  Write a program that asks the user to input two numbers and then compares them using 
# comparison operators (>, <, ==, !=)  to determine if the first number is greater than, less than, 
# equal to, or not equal to the second number. Display the results using Boolean values (True/False).

ip1 = int(input("Enter 1st number: "))
ip2 = int(input("Enter 2nd mumber: "))

if ip1>ip2:
    print("Input 1 is Greater than Input 2")
if ip1<ip2:
    print("Input 1 is Lesser than Input 2")
if ip1 == ip2:
    print("Input 1 and Input 2 is Equal")
if ip1 != ip2:
    print("Input 1 and Input 2 are not equal to each other")
