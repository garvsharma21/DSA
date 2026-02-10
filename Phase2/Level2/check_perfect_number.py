#Check if a number is a perfect number
def check_perfect_number(num):
    if num < 1:
        return False
    
    total_sum = 0
    i = 1

    while i < num:
        if num % i == 0:
            total_sum += i
        i += 1

    return total_sum == num



num = int(input("Enter a number: "))
if check_perfect_number(num):
    print("Perfect number")
else:
    print("Not a perfect number")