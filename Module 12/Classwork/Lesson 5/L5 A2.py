# Write a program to divide 2 numbers without using division operator.
def divide(dividend, divisor):
    sign = (-1 if (dividend < 0) ^ (divisor < 0) else 1) # 1 ^ 1 = 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1): # i = 31, 30, 29, ..., 0
        if (temp + (divisor << i) <= dividend): # 0 + (3 * 2**2) <= 13
            temp += divisor << i # 0 + 3 * 2**2 = 12
            quotient |= 1 << i # 0 or 1<<2 = 000 or 100 = 100 = 4

    if sign == -1:
        quotient = -quotient
    return quotient

a = int(input("Enter a for a/b: ")) # dividend
b = int(input("Enter b for a/b: ")) # divisor
print("Result of", a, "/", b, "is:", divide(a, b))

# a = 13 = 1101
# b = 3  = 0011