# Check if number is even or odd
def isEvenOdd(n):
    if(n ^ 1) == n + 1:
        return True
    else:
        return False
    
number = int(input("Enter yout number: "))
if isEvenOdd(number):
    print(number, "is Even")
else:
    print(number, "is Odd")