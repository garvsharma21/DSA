#Take a 4-digit number and check if the first and last digits are equal.

num = int(input("Enter a 4-digit number: "))

first_digit = num // 1000
last_digit = num % 10

if first_digit == last_digit:
    print("Both digits are equal")
else:
    print("Both digits are not equal")