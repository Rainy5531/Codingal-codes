# Algorith for finding all prime numbers up to any given limit
def Seive_of_Eratosthenes(num):
    prime = [True for i in range(0, num + 1)]
    p = 2
    while (p * p <= num):
    
        if (prime[p] == True):

            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, num + 1):
        if prime[p] == True:
            print(p, end=', ')

num = int(input("Enter an integer: "))
print("Following are the prime numbers smaller")
print("than or equal to", num)
Seive_of_Eratosthenes(num)