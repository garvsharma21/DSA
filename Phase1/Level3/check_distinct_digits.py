#Take a 3-digit number and check if all digits are distinct.

num = int(input("Enter a 3-digit number: "))

a = num % 10
b = (num // 10) % 10
c = (num // 100)

if a!=b and b!=c and c!=a:
    print("All the digits are distinct")
else:
    print("All the digits are not distinct")