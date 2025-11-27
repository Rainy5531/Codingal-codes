# Calculate value of x^y
def computePower(x, y):
    result = 1
    while y > 0: # 3, 2>0, 1>0
        if(y % 2 == 0): # 3%2=1, 2%2=0, 1%2=1
            x = x * x # 2*2=4
            y >>= 1 # 2 >> 1 = 10 >> 1 = 1
        else:
            result = result * x # 1 * 2 = 2, 4 * 2 = 8
            y -= 1 # 2, 0
    return result
x = int(input("Enter x for x^y: "))
y = int(input("Enter y for x^y: "))
print("Total : ", (computePower(x, y)))

# x = 2, y = 3