def consecutive(a):
    count = 0
    highest = 0
    while a > 0:
        if a & 1:
            count += 1
            highest = (count if count > highest else highest)
        else:
            count = 0
        a >>= 1
    return highest

num = int(input("Enter a number: "))
print("The highest number of consecutive 1s is:", consecutive(num))