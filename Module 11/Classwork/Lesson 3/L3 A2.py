def sum(n):
    return n*(n+1)/2

# Space complexity: theta(1), Auxiliary Space: theta(1)
# Linear space:

def arraysum(a):
    sum = 0
    for i in a:
        sum += i
    return sum

a = [12, 3, 4, 15]
arraysum(a)

# With the size of the array, the space also required increases
# Space complexity: theta(n), Auxiliary Space: theta(1)

def summ(n):
    if(n<=0):
        return
    return n+ summ(n-1)