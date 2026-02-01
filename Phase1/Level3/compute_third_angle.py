#Take two angles of a triangle and compute the third angle.

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))

#Check if angles are valid and logic
if (angle1 > 0 and angle1 <= 180) and (angle2 > 0 and angle2 <= 180):
    angle3 = 180 - (angle1 + angle2)
    print(angle3)
else:
    print("Angles are invalid to form a triangle")