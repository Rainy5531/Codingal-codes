# Counting the total number of bits
def numOfBits(n):
    count = 0
    while (n>0):
        count += 1
        n = n >> 1
    return count

n = int(input("Enter a number: "))
print("Number of bits: ", numOfBits(n))