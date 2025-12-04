#write a program to find the power set of a set
import math;

def printPowerSet(set, setSize):
    
    # Find the total elements possible in the power set
    powerSetSize = (int)(math.pow(2, setSize))

    for outer in range(0, powerSetSize):
        print("{", end = "")
        for inner in range(0, setSize):
            # Check if inner bit in the outer is set
            # If set then print inner element
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("}")

size = int(input("Enter array size : "))

lst = []
for i in range(0, size):
    n = int(input(f"Enter element no {i+1}: "))
    lst.append(n)

printPowerSet(lst, len(lst))