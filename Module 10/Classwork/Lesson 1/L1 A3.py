# Program to count number of items in the file
# Opening a file
file = open("Codingal.txt", "r")
Counter = 0

# Reading from file
Content = file.read()

# splitting content into lines
# and storing in a list
Colist = Content.split("\n")

print(Colist)
for i in Colist:
    if i:
        Counter += 1
print("This is the number of items in the file")
print(Counter)