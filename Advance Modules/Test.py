# odd even check
def checkEvenOdd(num):
    return "Even" if num % 2 == 0 else "Odd"


# prime check
def checkPrime(num):
    if num == 1: return "Not Prime"
    for i in range(2, num):
        if num % i != 0:
            return "Prime"

        else:
            return "Not Prime"


# fibonacci series
def fibonacciPrint(n):
    a = 0
    b = 1
    sum = 0
    print(a)
    print(b)
    for i in range(n):  # n=5
        sum = a + b  # sum=1
        a = b  # a=1
        b = sum  # b=2
        print(sum)


# print(checkEvenOdd(5))
# print(checkEvenOdd(6))
# print(checkPrime(7))
# print(checkPrime(10))
n = int(input("Enter the range: "))
fibonacciPrint(n)