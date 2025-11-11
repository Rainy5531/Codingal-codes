numLarge = int(input("Enter the larger number: "))
numSmall = int(input("Enter the smaller number: "))
i = 0

while True:
    i += 1
    multiple = numLarge * i
    if multiple % numSmall == 0:
        print(f"LCM of {numLarge} and {numSmall} is", multiple)
        break