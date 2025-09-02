n = int(input("enter number of rows: "))

for i in range(0, n): # i = 0,1,2,3,4, ... ,n-1

    for j in range(0, i+1): # j = 0,1,2,3,4, ... ,i

        print(" * ", end=" ")

    print("\n")