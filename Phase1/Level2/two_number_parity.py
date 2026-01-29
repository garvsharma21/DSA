#Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1%2==0 and num2%2==0:
    print("Both numbers are even.")
elif num1%2!=0 and num2!=0:
    print("Both numbers are odd")
else:
    print("One is even and the other one is odd.")