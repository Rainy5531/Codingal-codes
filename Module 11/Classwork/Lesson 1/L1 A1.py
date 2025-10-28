def fun1(n):
    return n*(n+1)/2
print(fun1(4))
# For this, the algorithm goes like this: (4*5)/2
# So the number of iterations will be 1 for any input

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum
print(fun2(4))
# For this, the algorithm goes like this: 1 + 2 + 3 + 4
# So the number of iterations will be n for any input

def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum+=1
    return sum
print(fun3(4))
# For this, the algorithm goes like this: 1 + (1+1) + (1+1+1) + (1+1+1+1)
# So the number of iterations will be n*(n+1)/2 for any input