# Write a program to check if a number is power of 2
def power2(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

n = int(input("Enter a number: "))
if power2(n):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")

'''
1 & 0 = 0
10 & 01 = 00
100 & 011 = 000
1000 & 0111 = 0000
10000 & 01111 = 00000
'''