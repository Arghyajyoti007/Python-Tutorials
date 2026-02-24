# Assignment 16: Create a Python program that takes two numbers as input 
# from the user and performs basic arithmetic operations (addition, subtraction, multiplication, division, 
# and modulus) on them. Display the results.

number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))

option = input("""Enter the Option : 
1 ---> Addition
2 ---> Subtraction
3 ---> Multiplication
4 ---> Division 
5 ---> Modulus
6 ---> Exit
""")

match option:
    case "1": 
        add = number1 + number2
        print(f"Addition : {add}")
    case "2":
        sub = number1 - number2
        print(f"Subtraction : {sub}")
    case "3": 
        mul = number1 * number2
        print(f"Multiplication : {mul}")
    case "4": 

        if number2 == 0 :
            print(0)
        else:
            div = number1 / number2
            print(f"Divition : {div}")
    case "5":
        mol = number1 % number2
        print(f"Modulus : {mol}")
    



