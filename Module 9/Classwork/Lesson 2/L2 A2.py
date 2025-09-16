# Empty Tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple having mixed data types
my_tuple = (1, "Hello", 3.4, [1, 2])
print(my_tuple)

# Nested Tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Accessing Tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])    # First element
print(my_tuple[-1])    # Last element

# Nested Tuple
n_tuple = ("mouse", [8, 4, 6, (1, 2, "abcd", {'1':2})], (1, 2, 3))

# Nested Tuple - Accessing element using index
print(n_tuple[0][3])        # 's'
print(n_tuple[1][1])     # 4
print(n_tuple[1][3][3]['1'])  # 2

# Slicing
print("Sliced :", my_tuple[1:4])

# Iterating through a Tuple
for letter in my_tuple:
    print("Hello", letter)