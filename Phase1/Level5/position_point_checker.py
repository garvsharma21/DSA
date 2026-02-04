#Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

if x == 0 and y == 0:
    print("Origin")
elif x != 0 and y == 0:
    print("X-Axis")
elif x == 0 and y != 0:
    print("Y-Axis")
else:
    print("Somewhere on the cartesian plane")