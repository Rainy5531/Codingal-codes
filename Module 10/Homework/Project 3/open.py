import os

with open('text.txt', 'r') as file:
    data = file.readlines()
    print('Words in this file are ....')
    for line in data:
        word = line.split()
        print(word)


print('\nChecking if My_File exists or not....')
if os.path.exists('My_File.txt'):
    print('My_File.txt exists!')
else:
    my_file = open('My_File.txt', 'x')
    my_file.write('Hello! My name is Hrishi. ! am 15 years old.')
    my_file.close()
    print('My_File.txt is created!')

if os.path.exists('sample_doc.txt'):
    os.remove('sample_doc.txt')
    print('sample_doc.txt is removed!')
else:
    print('sample_doc.txt does not exist!')