# Assignment 13: Palindrome Checker:
# Create a Python function that checks if a given string is a palindrome (reads the same forwards and backwards).
# Prompt the user for a string and use the function to determine if it's a palindrome.
# Display an appropriate message indicating whether the input is a palindrome or not.

def isPalindrome(input_string):
    reversed_string = input_string[::-1]
    if reversed_string == input_string:
        return  True
    else:
        return False

user_input = input("Please enter a string: ")
if isPalindrome(user_input):
    print("Entered String is a Palindrome")
else:
    print("Entered String is not a Palindrome")


