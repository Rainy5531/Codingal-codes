a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def multiply1(a, b):
    iterations = 0
    iterations += 1
    print("\nNumber of iterations:", iterations)
    return a * b
print(multiply1(a, b))

def multiply2(a, b):
    result = 0
    iterations = 0
    for i in range(0, b):
        iterations += 1
        result += a
    print("\nNumber of iterations:", iterations)
    return result
print(multiply2(a, b))