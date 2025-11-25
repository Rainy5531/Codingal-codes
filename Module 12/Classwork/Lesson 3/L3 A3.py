# Finding which number in the array appears odd number of times
# Assumption: Only two number appears odd number of times4

def TwoOdd(arr, size):

    xorof2, x, y, SetBit = arr[0], 0, 0, 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
    # xorof2 = 3
    SetBit = xorof2 & ~(xorof2 - 1) #11 & 01 = 01

    for i in range(size): # range(6), i = 0,1,2,3,4,5
        if (arr[i] & SetBit): # 11 & 01 = 01
            x = x ^ arr[i] # 000 ^ 011 = 011, 011 ^ 101 = 110, 110 ^ 011 = 101 = 5
        else:
            y = y ^ arr[i] # 000 ^ 110 = 110, 110 ^ 110 = 000, 000 ^ 110 = 110 = 6
    
    return x, y

arr = []
arr_size = int(input("Enter array size: "))
for i in range(arr_size):
    z = int(input("Enter number: "))
    arr.append(z)

x, y = TwoOdd(arr, arr_size)
print("TwoOdd elements are:", x, "and", y)

'''
[6,3,5,6,3,6]
[110,011,101,110,011,110]  (binary representation)
[110 ^ 000 = 110, 011 ^ 110 = 101, 101 ^ 101 = 000, 110 ^ 000 = 110, 011 ^ 110 = 101, 110 ^ 101 = 011 = 3]
'''