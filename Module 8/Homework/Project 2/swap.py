x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
z = int(input("Enter a number for z: "))

x = x + y + z
y = x - (y + z)
z = x - (y + z)
x = x - (y + z)

print("The numbers after swapping are:", x, y, z, "(x=first, y=second, z=third)")