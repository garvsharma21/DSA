#Check if one of the two given numbers is a multiple of the other.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >=0 and num2 >= 0:
    if num1 % num2 == 0:
        print(f"{num1} is a multiple of {num2}")
    elif num2 % num1 == 0:
        print(f"{num2} is a multiple of {num1}")
    else:
        print("Neither of the numbers are multiple of one another.")