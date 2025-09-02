num = int(input("Enter the number: "))

print(f"Table of {num}")

for i in range(1, 11): # i = 1,2,3,4,5,6,7,8,9,10
    mul = num*i
    print("%d x %d = %d" % (num, i, mul))