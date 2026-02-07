#Take three numbers and check if they are in geometric progression.

def check_gp(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return False
    
    if (num2//num1) == (num3//num2):
        return True
    else:
        return False

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if check_gp(num1, num2, num3):
    print("Numbers are in GP")
else:
    print("Numbers are not in GP")