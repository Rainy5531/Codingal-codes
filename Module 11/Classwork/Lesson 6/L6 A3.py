'''
Find and print all numbers from 1 to 3000 that are bothe:
- Prime numbers
- Palindrome numbers
'''

a = int(input("Enter number: "))

for num in range(1, a + 1):
    factors = 0
    reverse = 0
    temp = num

    # Checking prime
    for i in range(1, temp + 1):
        if temp % i == 0:
            factors += 1

    if factors == 2:
        # Checking palindrome
        while temp > 0:
            reverse = reverse * 10 + (temp % 10)
            temp //= 10

        if reverse == num:
            print(num, end=', ')