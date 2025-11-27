# Reversing the bits of a number

def reverse(num):
    res = 0
    while num > 0:
        res = (res << 1) | (num & 1)
        num = num >> 1
    return res

num = int(input("Enter a number to reverse its bits: "))
reversed = reverse(num)
print("Reversed bits number is:", reversed)