# Check if number is power of 4
def power4(num):
    # Check if number is positive and is a power of 2
    if num <= 0 or (num & (num - 1)) != 0:
        return False
    
    count = 0
    while num > 1:
        num >>= 1
        count += 1

    # Check if the only set bit is at an even position
    return count % 2 == 0

number = int(input("Enter a number: "))
if power4(number):
    print(number, "is a power of 4")
else:
    print(number, "is not a power of 4")

'''
1 & 0 = 0 - power of 4
10 & 01 = 00 - not power of 4
100 & 011 = 000 - power of 4
1000 & 0111 = 0000 - not power of 4
10000 & 01111 = 00000 - power of 4
'''