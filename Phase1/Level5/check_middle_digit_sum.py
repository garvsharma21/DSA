#Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.

def check_middle_digit_sum(num):
    if num < 100 or num > 999:
        return False
    
    c = num % 10
    b = (num // 10) % 10
    a = num // 100

    if b == a + c:
        return True
    else:
        return False

num = int(input("Enter the number: "))

if check_middle_digit_sum(num):
    print("Sum of first and third digit is equal to the middle")
else:
    print("Sum of first and third digit is not equal to the middle")