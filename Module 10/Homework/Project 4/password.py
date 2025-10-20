import random
import string

l = input("Enter the desired password length : ")
l = int(l)
def generate_password(length = l):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
password = generate_password(l)
print(password)