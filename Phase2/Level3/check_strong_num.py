#Check if a number is a strong number (sum of factorials of digits = number).

def factorial(num):
    i = 1

    if num < 0:
        return -1
    elif num == 0:
        return 1

    while num != 0:
        i = i * num
        num = num - 1

    return i

def check_strong_number(num):
    sum = 0

    if num <= 0:
        return -1
    
    original_num = num

    while num != 0:
        digit = num % 10
        sum = sum + factorial(digit)
        num = num // 10

    if sum == original_num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if check_strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")