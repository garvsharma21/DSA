#Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 

num = int(input("Enter a 3-digit number: "))

a = num % 10
b = (num // 10) % 10
c = num // 100

if b > a and b > c:
    print(f"{b} is the largest number")
elif a > b and c > b:
    print(f"{b} is the smallest number")
    
else:
    print(f"{b} is neither largest nor smallest number")