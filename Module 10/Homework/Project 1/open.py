file = open('open.txt', 'w')
file.write('Hello World!')
file.close()

file = open('open.txt', 'r')
print(file.read())
file.close()

file = open('open.txt', 'a')
file.write('\nWelcome to Codingal!')
file.close()

file = open('open.txt', 'r')
print(file.read())
file.close()