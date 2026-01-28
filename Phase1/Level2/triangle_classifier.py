#If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

side_a = float(input("Enter length of side a: "))
side_b = float(input("Enter length of side b: "))
side_c = float(input("Enter length of side c: "))

#Check for Valid Triangle
if side_a<=0 or side_b<=0 or side_c<=0:
    print("Invalid triangle")
else:
    max_side = max(side_a, side_b, side_c)

#Check for Equilateral Triangle
if side_a!=side_b or side_b!=side_c or side_c!=side_a:
    print("Not an equilateral triangle")
else:
    print("Equilateral triangle")

#Check for Isosceles Triangle
if (side_a!=side_b and side_b==side_c) or (side_b!=side_c and side_a==side_c) or (side_c!=side_a and side_a==side_b):
    print("Isosceles triangle")
else:
    print("Not an isosceles Triangle")

#Check for Scalar Triangle:
if side_a==side_b or side_b==side_c or side_a==side_c:
    print("Not a scalene triangle")
else:
    print("Scalene Triangle")