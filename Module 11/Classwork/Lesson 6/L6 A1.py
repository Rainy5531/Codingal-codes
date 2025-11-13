# Program to check if a number is prime or now
from math import sqrt

number = int(input("Enter a number: "))
print("\n")

# If given number is greater than one
if number > 1:

    # Check if number is divisible from 2 to sqrt(number)
    for i in range(2, int(sqrt(number)) + 1):

        # If divisible by any number it is a non-prime number
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")