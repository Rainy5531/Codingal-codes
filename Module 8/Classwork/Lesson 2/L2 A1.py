name = "Penguin" #string datatype
age = 15 #integer datatype
is_student = True #boolean datatype True/False
weight = 38.5 #float datatype

print("Name :", name)
print("Data type of Name is ", type(name))
print("Age :", age)
print("Data type of Age is ", type(age))
print("Is Student :", is_student)
print("Data type of Is Student is ", type(is_student))
print("Weight :", weight)
print("Data type of Weight is ", type(weight))

print("\n After Type Casting....")
age = str(age)
print(age)
print("Data type of age is", type(age))
weight = int(weight)
print(weight)
print("Data type of weight is", type(weight))