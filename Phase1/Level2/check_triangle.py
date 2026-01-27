side_a = float(input("Enter length of side a: "))
side_b = float(input("Enter length of side b: "))
side_c = float(input("Enter length of side c: "))

if side_a > 0 and side_b > 0 and side_c > 0:
    if side_a >= side_b and side_a >= side_c:
        max_length_side = side_a
    elif side_b >= side_a and side_b >= side_c:
        max_length_side = side_b
    else:
        max_length_side = side_c

    triangle_perimeter = side_a + side_b + side_c
    
    if triangle_perimeter - max_length_side > max_length_side:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

else:
    print("Enter non-zero or positive value for a side")


