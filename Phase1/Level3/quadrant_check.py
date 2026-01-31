#Take coordinates (x, y) and determine which quadrant the point lies in.

x = int(input("Enter the first coordinate (x): "))
y = int(input("Enter the second coordinate (y): "))

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
else:
    print("Origin")