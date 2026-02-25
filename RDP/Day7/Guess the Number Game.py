# Assignment 33: Guess the Number Game
# Create a number guessing game in Python. The computer selects a random number between 1 and 100, and the user has to guess the number.
# Use a while loop to keep the game running until the user guesses the correct number.
import random

random_integer = random.randint(1,100)

while True:
    user_integer = int(input("Enter a number between 1 and 100: "))

    if user_integer > random_integer:
        print("Guess Lower!!")
    elif user_integer < random_integer:
        print("Guess Upper!!")
    else:
        print("You Won!!")
        break



