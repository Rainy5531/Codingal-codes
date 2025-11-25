# check if  numbers are equal or not
def checkIfSame(num1, num2):
    if((num1 ^ num2) != 0):
        print("Numbers are not equal")

    else:
        print("Both numbers are equal")

num1 = int(input("Enter first number to compare: "))
num2 = int(input("Enter second number to compare: "))
checkIfSame(num1, num2)