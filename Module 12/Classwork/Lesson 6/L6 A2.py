# Find the number of bits needed to be flipped to make the two numbers equal
def flips(num1, num2):
    flips = 0
    while(num1 > 0 or num2 > 0):
        t1 = num1 & 1
        t2 = num2 & 1
        if t1 != t2:
            flips += 1
        num1 >>= 1
        num2 >>= 1
    return flips
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Number of flips needed: ", flips(num1, num2))