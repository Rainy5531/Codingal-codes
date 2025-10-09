# Program to copy odd lines of one file to another
# open file in read mode
fn = open('Codingal.txt', 'r')

# open other file in write mode
fn1 = open('Codingal2.txt', 'w')

# read the content of the file line by line
cont = fn.readlines()
print(cont)
for i in range(1, len(cont)+1): # i = 1,2,3,4
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass

# close the file
fn1.close()

# open file in read mode
fn1 = open('Codingal2.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all the files
fn.close()
fn1.close()