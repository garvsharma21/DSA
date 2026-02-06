#Take three numbers and check if they can form a Pythagorean triplet.

#The main issue is I haven't checked for positive numbers here.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest_number = None

#Caluculate largest number
if num1 >= num2 and num1 >= num3:
    largest_number = num1
elif num2 >= num1 and num2 >= num3:
    largest_number = num2
else:
    largest_number = num3

#Condition for Pythagorean Triplet
if ((num1**2 + num2**2 + num3**2) - (largest_number**2)) == (largest_number)**2:
    print("Pythagorean triplet")
else:
    print("Not a pythagorean triplet")