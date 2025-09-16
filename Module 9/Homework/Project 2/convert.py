t1 = (1, "codingal", 3.4)
print("Tuple: ", t1)
l1 = list(t1)
print("List: ", l1)

# Another way
t2 = (1, 2, 3, 4, 5)
print("\nSecond Tuple: ", t2)
l2 = []
for i in t2:
    l2.append(i)
print("Second List: ", l2)

# Another way
t3 = (1, 2, 3, 4)
print("\nThird Tuple: ", t3)
#list conprehension
print("Third List: ", [i for i in t3])