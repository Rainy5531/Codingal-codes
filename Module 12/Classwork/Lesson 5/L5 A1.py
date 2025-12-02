# Swapping 2 numbers
def swap(a, b): # a = 2, b = 3
    a = a^b # a = 10 ^ 11 = 01
    b = a^b # b = 01 ^ 11 = 10 = 2
    a = a^b # a = 01 ^ 10 = 11 = 3
    print("After swapping: a =", a, "b =", b)

def swap2(a, b):
    a = (a&b) + (a|b) # (10 & 11) + (10 | 11) = 10 + 11 = 101
    b = a + (~b) + 1 # a + (-b-1) + 1 = a - b = 5 - 3 = 2
    a = a + (~b) + 1 # a + (-b-1) + 1 = a - b = 5 - 2 = 3
    print("After swapping: a =", a, "b =", b)

swap(10, 20)
swap2(10, 20)

# ~b = -b-1