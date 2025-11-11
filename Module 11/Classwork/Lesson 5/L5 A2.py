# Program to finr HCF/GCD

# Enter two numbers

numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
num1 = numberLargest
num2 = numberSmallest

# Usinf Euclidean Algorithm
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print(f"HCF of {num1} and {num2} is : ", numberLargest)


#(12,8) --> (8,4) --> (4,0) --> HCF = 4