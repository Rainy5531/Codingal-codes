# PART 1
import numpy as np
from numpy import random

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1[0])
print(arr1[2:4])
for i in arr1:
    print(i)

arr2 = np.array([[1, 2, 3, 5], [3, 4, 5, 6]])
print(arr2.shape)
print(arr2.reshape(8,1))

arr3 = np.array([1, 2, 3, 4, 4])

arr = np.concatenate((arr1, arr3))
print(arr)

x = np.where(arr == 4)
print(x)
print(np.sort(arr))

print(random.randint(100)) # 0 - 99

print(np.arange(3)+1)

# PART 2
data_type = [('name', 'S15'), ('class', int), ('height', float)] # S15 means string of max length 15

# the actual data, matching the defined structure
student_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.1), ('Pit', 6, 40.11)]

# Create the structured array
students = np.array(student_details, dtype=data_type)

print("Original Array:")
print(students)

print("\nSort by height")
sorted_students = np.sort(students, order='height') # The np.sort() function returns a *new* sorted array, it doesn't modify the original.
print(sorted_students)





# *** Extra ***
print(np.linspace(0,1,5)) # 5 equally spaced numbers between 0 and 1

# Special arrays
print(np.zeroes((2,3))) # 2x3 matrix of zeroes
print(np.ones((3,3)))   # 3x3 matrix of ones
print(np.eye(3))        # 3x3 identity matrix

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)        # element-wise addition
print(a * b)        # element-wise multiplication
print(np.dot(a, b)) # dot product (scalar)
print(np.mean(a))   # average of elements
print(np.std(a))    # standard deviation of elements
print(np.sum(a))    # sum of elements