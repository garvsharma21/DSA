#Take three numbers and print the median value (neither maximum nor minimum).

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number:  "))

if (num1 >= num2 and num2 >= num3) or (num3 >= num2 and num2 >= num1):
    print(f"Median: {num2}")
elif (num1 >= num3 and num3 >= num2) or (num2 >= num3 and num3 >= num1):
    print(f"Median: {num3}")
else:
    print(f"Median: {num1}")