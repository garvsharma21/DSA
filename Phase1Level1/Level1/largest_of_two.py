#Take two numbers and print the largest one

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >= num2:
    print(f"{num1} is greater than or equal to {num2}")
else:
    print(f"{num2} is greater than {num1}")