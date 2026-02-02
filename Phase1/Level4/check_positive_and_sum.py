#Take two numbers and check if both are positive and their sum is less than 100.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

if num1 > 0 and num2 > 0 and sum > 100:
    print("Numbers are positive and their sum is greater than 100.")
else:
    print("Error 404")