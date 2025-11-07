binary = int(input("Enter a binary number: "))

check = binary
is_binary = True
while check > 0:
    digit = check % 10
    if digit != 0 and digit != 1:
        is_binary = False
        break
    check //= 10

decimal = 0
length = len(str(binary))

if is_binary:
    for i in range(0, length):
        digit = binary % 10
        decimal += digit * (2 ** i)
        binary //= 10   
    print("The decimal equivalent is:", decimal)
else: print("Error: The input is not a valid binary number.")