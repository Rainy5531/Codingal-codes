# open the file in read mode
file_read = open('Codingal2.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Codingal2.txt', 'w')
# write in the file
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old.")
file_write.close()

# open the file in append mode
file_append = open('Codingal2.txt', 'a')
# append in the file
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old.")
file_append.close()

'''
Original text in Codingal2.txt
--------------------------------
Codingal is on a mission to inspire school kids to fall in love with coding.
While still in school, those who start young will be ahead of everyone by the time they get into college.
'''