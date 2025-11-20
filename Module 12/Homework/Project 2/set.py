def rightmost(num):
    position = 0

    while num > 0:
        if num & 1:
            position += 1
            print("The position of the rightmost set bit is:", position)
            break
        else:
            num = num >> 1
            position += 1
    else:
        print("No set bits found")

num = int(input("Enter a number: "))
rightmost(num)