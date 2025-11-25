# Finding which numbers from the array appear odd number of times
# Assumption: Only one number appears odd number of times

def OddOccurance(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n = int(input("Enter array size: "))
while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n -= 1
print("Odd occuring number is:", OddOccurance(arr))

'''
[6, 3, 5, 3, 6]
[110, 011, 101, 011, 110]  (binary representation)
[110 ^ 000 = 110, 011 ^ 110 = 101, 101 ^ 101 = 000, 011 ^ 000 = 011, 110 ^ 011 = 101 = 5]
'''