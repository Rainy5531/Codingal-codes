# program to append contents of file in another file

# entering the file names
firstfile = input("Enter the name of the first file: ")
secondfile = input("Enter the name of the second file: ")

# opening the files in read only mode to read initial contents
f1 = open(firstfile, "r")
f2 = open(secondfile, "r")

# printing the contents of the file before appending
print("Contents of the first file before appending -\n", f1.read())
print("Contents of the second file before appending -\n", f2.read())

# closing files
f1.close()
f2.close()

# opening the first file in append mode and the second file in read mode
f1 = open(firstfile, "a+") # the '+' lets it be read as well
f2 = open(secondfile, "r")

# appending the contents of the second file to the first file
f1.write("\n" + f2.read())

# relocating the cursor to the beginning of both files
f1.seek(0)
f2.seek(0)
# files can only be read if the cursor is at the beginning

# printing the contents of the file after appending
print("Contents of the first file after appending -\n", f1.read())
print("Contents of the second file after appending -\n", f2.read())

# closing the files
f1.close()
f2.close()