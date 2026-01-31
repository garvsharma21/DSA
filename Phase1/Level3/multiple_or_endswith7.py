#Check if a number is a multiple of 7 or ends with 7.

num = int(input("Enter a number: "))

end_digit = num % 10

if num % 7 == 0 or end_digit == 7:
    print(f"{num} is a multiple of 7 or ends with 7.")