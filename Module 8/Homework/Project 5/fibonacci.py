def fibonacci(n):
    num1 = 0
    num2 = 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto", n, ":")
        print(num1)
    else:
        print("Fibonacci sequence upto", n, ":")
        while count < n:
            print(num1)
            nth = num1 + num2
            num1 = num2
            num2 = nth
            count += 1
    
num = int(input("Enter a positive integer: "))
fibonacci(num)