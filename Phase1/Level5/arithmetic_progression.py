#Take three numbers and check if they are in arithmetic progression.

def check_ap(num1, num2, num3):
    if num2 - num1 == num3 - num2:
        return True
    else:
        return False

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if check_ap(num1, num2, num3):
    print("The numbers are in AP.")
else:
    print("The numbers are not in AP.")