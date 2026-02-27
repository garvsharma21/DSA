#Check if a number is palindrome using recursion

def check_palindrome(num, rev=0):
    if num == 0:
        return rev

    return check_palindrome(num // 10, num%10 + rev * 10)

num = int(input("Enter a positive number: "))
result = check_palindrome(num)

if result == num:
    print(f"Number is palindrome")
else:
    print("Number is not palindrome")
