# Program to finr HCF/GCD

# Enter two numbers

numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))

# Usinf Euclidean Algorithm
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print(f"HCF of {numberLargest} and {numberSmallest} is : ", numberLargest)


#(12,8) --> (8,4) --> (4,0) --> HCF = 4