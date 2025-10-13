file = open("text.txt", "r")
print(file.read())
file.close()

file = open('text.txt', 'r')
print('\n\n')
print(file.read(10))
file.close()

file = open('text.txt', 'r')
print('\n\n')
print(file.readline())
file.close()

file = open('text.txt', 'r')
print('\n\n')
for i in range(4):
    print(file.readline())
file.close()

file = open('text.txt', 'r')
print('\n\n')
for line in file:
    print(line)
file.close()