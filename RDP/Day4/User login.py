# Assignment 18: Build a program that simulates a simple access control system.
# Prompt the user for a username and password.
# Then, use logical operators (and, or, not) to determine whether the user should be granted access or denied access
# based on predefined username and password criteria. Provide appropriate feedback to the user.

username_db = "Arghya_Jyoti"
password_db = "259344"


def user_access_control(username):
    if username in username_db:
        password = input("Enter your password: ")
        if password == password_db:
            print("Login successful")
        else:
            print("Wrong Credentials")

    else:
        print("Wrong Credentials")


username = input("Enter your username: ")
user_access_control(username)

