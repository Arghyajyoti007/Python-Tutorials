# Assignment 4: Simple Interest Calculator
# Write a program that calculates the simple interest for a given principal amount, rate of interest, and time period.
# The formula for simple interest is: Simple Interest = (principal * rate * time) / 100.
# Take principal ,rate , time from user.

principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
time = year + month / 12
simple_interest = (principal * rate * time) / 100
print("Simple Interest: ", simple_interest)
print("Maturity Ammount : ", principal + simple_interest)

