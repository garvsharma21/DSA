#Check if a number is an Armstrong number.

def calculate_num_of_digits(num):
    num = abs(num)

    if num == 0:
        return 1
    
    count = 0

    while num != 0:
        count += 1
        num = num // 10

    return count

def check_armstrong_number(num):
    num = abs(num)

    if num == 0:
        return True

    count = calculate_num_of_digits(num)

    total_sum = 0
    original_num = num

    while num != 0:
        digit = num % 10
        total_sum = total_sum + digit**count
        num = num // 10

    return total_sum == original_num

num = int(input("Enter a number: "))

if check_armstrong_number(num):
    print("Armstrong Number")
else:
    print("Not an armstrong number")