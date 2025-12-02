def power8(num):
    if num <= 0 or (num & (num - 1)) != 0:
        return False
    
    count = 0
    while num > 1:
        num >>= 1
        count += 1
    return count % 3 == 0

n = int(input("Enter a number: "))
if power8(n):
    print("\nThe number is a power of 8")
else:
    print("\nThe number is not a power of 8")

'''
1 & 0 = 0 - power of 8
10 & 01 = 00 - not power of 8
100 & 011 = 000 - not power of 8
1000 & 0111 = 0000 - power of 8
10000 & 01111 = 00000 - not power of 8
100000 & 011111 = 000000 - not power of 8
1000000 & 0111111 = 0000000 - power of 8
'''