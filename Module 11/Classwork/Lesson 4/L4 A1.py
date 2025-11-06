# Program to find if a number is armstrong number or not

# Take input from user
num = int(input("Input your number: "))

# Calculate number of digits
digits = len(str(num))

# Initialize result variable
result = 0

# find the sum of the a^digits of each digit
temp = num
while temp > 0:
    digit = temp % 10
    result +=digit ** digits
    temp //= 10

# display the result
if num == result:
    print(num, "Is an Armstrong number")
else:
    print(num, "Is not an Armstrong number")

# 153 = 1 ** (len(num)) + 5 ** (len(num)) + 3 ** (len(num))
# 153 = 1 ** 3 + 5 ** 3 + 3 ** 3
# 153 = 1 + 125 + 27
# 153 = 153