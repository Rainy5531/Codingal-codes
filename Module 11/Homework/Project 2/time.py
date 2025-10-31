def myfunction(n):
    iteration = 0
    for i in range(0, n+1):
        print("First Loop")
        iteration += 1
    
    j = 1
    while(j <= n):
        print("Second Loop", j)
        j = j * 2
        iteration += 1

    for i in range(0, 100):
        print("Third Loop")
        iteration += 1
    print("\nWhen n is", n, "iterations =", iteration, "\n")
    print("The time complexity is O(n)")

myfunction(10)
myfunction(100)