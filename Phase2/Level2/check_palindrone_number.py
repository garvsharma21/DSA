#Check if a number is a palindrome

def check_palindrome_number(num):
    num = abs(num)
    
    if num == 0:
        return True

    rev_num = 0
    original_num = num

    while num != 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10

    return original_num == rev_num

num = int(input("Enter a number: "))

if check_palindrome_number(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")