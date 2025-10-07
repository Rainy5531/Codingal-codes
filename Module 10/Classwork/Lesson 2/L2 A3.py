# Program to remove lines starting with any prefix

file1 = open('Codingal.txt', 'r')
file2 = open('Codingal2.txt', 'w')

# reading each line from original text file
for line in file1.readlines():

    # reading all lines that do not begin with "Coding"
    if not (line.startswith("Coding")):
        
        # printing those lines
        print(line)

        # storing only those lines that do not begin with "Coding"
        file2.write(line)

# close and save the files
file1.close()
file2.close()